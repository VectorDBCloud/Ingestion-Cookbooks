import random
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# Define the collection schema
dim = 128  # dimension of embedding vector
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=200),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dim)
]
schema = CollectionSchema(fields, "A sample book collection")

# Create the collection
collection_name = "book_collection"
collection = Collection(collection_name, schema)

# Create an IVF_FLAT index for the embedding field
index_params = {
    "metric_type": "L2",
    "index_type": "IVF_FLAT",
    "params": {"nlist": 1024}
}
collection.create_index("embedding", index_params)

# Generate some sample data
num_entities = 1000
entities = [
    [i for i in range(num_entities)],  # id
    [f"Book Title {i}" for i in range(num_entities)],  # title
    [[random.random() for _ in range(dim)] for _ in range(num_entities)]  # embedding
]

# Insert the entities
collection.insert(entities)

# Flush the collection to ensure data is written to disk
collection.flush()

print(f"Inserted {num_entities} entities into the '{collection_name}' collection.")

# Perform a vector similarity search
search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
results = collection.search(
    data=[[random.random() for _ in range(dim)]],  # query vector
    anns_field="embedding",
    param=search_params,
    limit=5,
    expr=None,
    output_fields=["title"]
)

print("\nSearch Results:")
for hits in results:
    for hit in hits:
        print(f"Title: {hit.entity.get('title')}, Distance: {hit.distance}")

# Disconnect from Milvus
connections.disconnect("default")

print("\nMilvus ingestion and search completed successfully.")
