import chromadb
from chromadb.config import Settings
import numpy as np

# Initialize ChromaDB client
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

# Create or get a collection
collection_name = "my_collection"
collection = client.get_or_create_collection(name=collection_name)

# Sample data
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "To be or not to be, that is the question",
    "All that glitters is not gold"
]
metadatas = [
    {"source": "english_proverb", "year": 1800},
    {"source": "chinese_proverb", "year": 500},
    {"source": "shakespeare", "year": 1600},
    {"source": "shakespeare", "year": 1600}
]
ids = ["doc1", "doc2", "doc3", "doc4"]

# Function to create dummy embeddings (replace with actual embedding function)
def get_embeddings(texts):
    return [np.random.rand(384).tolist() for _ in texts]

# Get embeddings
embeddings = get_embeddings(documents)

# Add data to the collection
collection.add(
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)

print(f"Added {len(documents)} documents to ChromaDB collection '{collection_name}'")

# Query example
query_text = "What did Shakespeare write?"
query_embedding = get_embeddings([query_text])[0]

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print("\nQuery Results:")
for i, (doc, metadata, distance) in enumerate(zip(results['documents'][0], results['metadatas'][0], results['distances'][0])):
    print(f"{i+1}. Document: {doc}")
    print(f"   Metadata: {metadata}")
    print(f"   Distance: {distance}\n")

# Persist the changes
client.persist()
print("Changes persisted to disk")
