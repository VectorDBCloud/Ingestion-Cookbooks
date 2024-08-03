import os
import sys
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from sentence_transformers import SentenceTransformer

def main():
    # Get API URL and key from environment variables
    API_URL = os.getenv('VECTORDBCLOUD_MILVUS_API_URL')
    API_KEY = os.getenv('VECTORDBCLOUD_MILVUS_API_KEY')

    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    try:
        # Connect to Milvus
        connections.connect("default", uri=API_URL, token=API_KEY)

        # Initialize the sentence transformer model from Hugging Face
        model = SentenceTransformer('all-MiniLM-L6-v2')
        dim = model.get_sentence_embedding_dimension()

        # Define the collection schema
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
        titles = [f"Book Title {i}" for i in range(num_entities)]
        embeddings = model.encode(titles).tolist()

        entities = [
            [i for i in range(num_entities)],  # id
            titles,  # title
            embeddings  # embedding
        ]

        # Insert the entities
        collection.insert(entities)

        # Flush the collection to ensure data is written to disk
        collection.flush()

        print(f"Inserted {num_entities} entities into the '{collection_name}' collection.")

        # Perform a vector similarity search
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        query = "A book about adventure"
        query_embedding = model.encode([query]).tolist()[0]

        results = collection.search(
            data=[query_embedding],  # query vector
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

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
