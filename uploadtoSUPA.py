# this file will extract the vendor id and company description from the csv file and store it in supabase table

import pandas as pd
from supabase import create_client
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Initialize LangChain embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=OPENAI_API_KEY
)

def get_embedding(text):
    """Get embedding for text using LangChain."""
    try:
        embedding = embeddings.embed_query(text)
        return embedding
    except Exception as e:
        print(f"Error generating embedding: {str(e)}")
        raise

def get_structured_vendor_data(df):
    """Convert vendor data to a structured format for the agent."""
    vendors = []
    for _, row in df.iterrows():
        description = row["Description"]
        vendor = {
            "vendor_id": row["vendor_id"],
            "company_description": description,
            "embedding": get_embedding(description),
            "email": row["Email id"],
            "vendor_name": row["Vendor name"],
        }
        vendors.append(vendor)
    return vendors

def store_vendor_data(vendors):
    """Store vendor data in Supabase."""
    total = len(vendors)
    for idx, vendor in enumerate(vendors, 1):
        try:
            response = supabase.table("new_vendors").insert([vendor]).execute()
            print(f"[{idx}/{total}] Successfully stored vendor {vendor['vendor_id']} in Supabase")
        except Exception as e:
            print(f"[{idx}/{total}] Error storing vendor {vendor['vendor_id']}: {str(e)}")

if __name__ == "__main__":
    # Read the CSV file
    df = pd.read_csv('Merged_Data.csv')
    
    # Skip the first 5 rows that were already uploaded
    df = df.iloc[5:]
    print(f"Processing {len(df)} remaining rows...")

    # Get structured data with embeddings
    vendor_data = get_structured_vendor_data(df)

    # Store data in Supabase
    store_vendor_data(vendor_data)

    # Print the results
    print("\nStructured Vendor Data:")
    for vendor in vendor_data:
        print(f"Vendor ID: {vendor['vendor_id']}")
        print(f"Description: {vendor['company_description']}")
        print(f"Email: {vendor['email']}")
        print(f"Embedding Generated: Yes")
        print("-" * 50)