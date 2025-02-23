# this file will search for similar vendors based on the company description

import os
from dotenv import load_dotenv
from supabase import create_client
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

def search_similar_vendors(query, limit=15):
    """
    Search for vendors with similar descriptions to the query.
    Returns the top matching vendors sorted by similarity.
    
    Args:
        query (str): The search query
        limit (int): Maximum number of results to return
    """
    try:
        # Generate embedding for the query
        query_embedding = embeddings.embed_query(query)
        
        # Call the match_vendors function
        response = supabase.rpc(
            'match_vendors',
            {
                'query_embedding': query_embedding,
                # 'match_threshold': similarity_threshold,
                'match_count': limit
            }
        ).execute()
        
        # Extract and format results
        results = []
        for match in response.data:
            results.append({
                'vendor_id': match['vendor_id'],
                'description': match['company_description'],
                'email': match['email'],
                'similarity_score': match['similarity']
            })
            
        return results
        
    except Exception as e:
        print(f"Error performing similarity search: {str(e)}")
        raise

def print_search_results(results):
    """Print search results in a readable format."""
    if not results:
        print("\nNo matching vendors found.")
        return

    print("\nSearch Results:")
    print("-" * 80)
    for idx, result in enumerate(results, 1):
        print(f"Match #{idx}")
        print(f"Vendor ID: {result['vendor_id']}")
        print(f"Email: {result['email']}")
        print(f"Similarity Score: {result['similarity_score']:.4f}")
        print(f"Description: {result['description']}")
        print("-" * 80)

if __name__ == "__main__":
    # Get search query from user
    query = input("Enter your search query: ")
    
    # Perform similarity search
    results = search_similar_vendors(
        query,
        limit=15,
        # similarity_threshold=0.5  # Adjust this threshold as needed (0 to 1)
    )
    
    # Print results
    print_search_results(results)
