import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.http import models

# Initialize Qdrant client
client = QdrantClient("localhost", port=6333)

# Define collection name
collection_name = "my_collection"

# Create a new collection
client.recreate_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
)

# Generate sample data
num_vectors = 1000
vector_size = 768

vectors = np.random.rand(num_vectors, vector_size).tolist()
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
query_vector = np.random.rand(vector_size).tolist()
search_result = client.search(
    collection_name=collection_name,
    query_vector=query_vector,
    limit=5
)

print("\nSample search results:")
for scored_point in search_result:
    print(f"ID: {scored_point.id}, Score: {scored_point.score}, Payload: {scored_point.payload}")
