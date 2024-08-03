import os
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

# Initialize Qdrant client
client = QdrantClient(url=API_URL, api_key=API_KEY)

# Initialize the sentence transformer model from Hugging Face
model = SentenceTransformer('all-MiniLM-L6-v2')
vector_size = model.get_sentence_embedding_dimension()

# Define collection name
collection_name = "my_collection"

# Create a new collection
client.recreate_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
)

# Generate sample data
num_vectors = 1000
sample_texts = [f"This is sample text number {i}" for i in range(num_vectors)]
vectors = model.encode(sample_texts).tolist()
payloads = [{"metadata": f"Data point {i}"} for i in range(num_vectors)]

# Prepare points for insertion
points = [
    models.PointStruct(
        id=i,
        vector=vector,
        payload=payload
    )
    for i, (vector, payload) in enumerate(zip(vectors, payloads))
]

# Insert points in batches
batch_size = 100
for i in range(0, len(points), batch_size):
    batch = points[i:i+batch_size]
    client.upsert(
        collection_name=collection_name,
        points=batch
    )

print(f"Inserted {num_vectors} vectors into Qdrant collection '{collection_name}'")

# Perform a sample search
query_text = "Sample query text"
query_vector = model.encode([query_text])[0].tolist()
search_result = client.search(
    collection_name=collection_name,
    query_vector=query_vector,
    limit=5
)

print("\nSample search results:")
for scored_point in search_result:
    print(f"ID: {scored_point.id}, Score: {scored_point.score}, Payload: {scored_point.payload}")

print("\nQdrant ingestion and search completed successfully.")
