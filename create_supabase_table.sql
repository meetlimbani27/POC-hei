-- Enable the vector extension if not already enabled
CREATE EXTENSION IF NOT EXISTS vector;

-- Create the new_vendors table
CREATE TABLE IF NOT EXISTS new_vendors (
    id BIGSERIAL PRIMARY KEY,
    vendor_id TEXT NOT NULL UNIQUE,
    company_description TEXT,
    company_name TEXT,
    contact_number TEXT,
    email TEXT,
    vendor_name TEXT,
    embedding vector(1536),  -- OpenAI's text-embedding-ada-002 uses 1536 dimensions
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Create an index on vendor_id for faster lookups
CREATE INDEX IF NOT EXISTS idx_new_vendors_vendor_id ON new_vendors(vendor_id);

-- Create a vector similarity search index
CREATE INDEX IF NOT EXISTS idx_new_vendors_embedding ON new_vendors 
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- Drop existing function if it exists
DROP FUNCTION IF EXISTS match_vendors(vector(1536), float, int);

-- Create the match_vendors function for similarity search
CREATE OR REPLACE FUNCTION match_vendors (
  query_embedding vector(1536),
  match_threshold float,
  match_count int
)
RETURNS TABLE (
  vendor_id text,
  company_description text,
  vendor_name text,
  email text,
  similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    v.vendor_id,
    v.company_description,
    v.vendor_name,
    v.email,
    1 - (v.embedding <=> query_embedding) as similarity
  FROM new_vendors v
  WHERE 1 - (v.embedding <=> query_embedding) > match_threshold
  ORDER BY v.embedding <=> query_embedding ASC
  LIMIT LEAST(match_count, 200);
END;
$$;

-- Disable RLS temporarily for data upload
ALTER TABLE new_vendors DISABLE ROW LEVEL SECURITY;

-- Note: After data upload, you can re-enable RLS and set policies with:
-- ALTER TABLE new_vendors ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "Enable read for authenticated users" ON new_vendors FOR SELECT TO authenticated USING (true);
