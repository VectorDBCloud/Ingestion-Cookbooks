# Ingestion Cookbook

This repository contains a collection of scripts for ingesting data into various vector databases using open-source embeddings. It serves as a cookbook with recipes (scripts) for advanced data ingestion techniques and similarity search.

## Supported Vector Databases

- [pgvector](pgvector/): PostgreSQL extension for vector similarity search
- [Milvus](milvus/): Cloud-native vector database for similarity search
- [ChromaDB](chromadb/): Open-source embedding database
- [Qdrant](qdrant/): Vector database for next-gen AI applications

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/VectorDBCloud/Ingestion-Cookbooks.git
   cd Ingestion-Cookbooks
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables for the Vector Database Cloud API:
   ```
   export VECTORDBCLOUD_API_URL=your_api_url
   export VECTORDBCLOUD_API_KEY=your_api_key
   ```
   Note: Specific environment variable names may vary for each database. Check the individual scripts for details.

4. Navigate to the specific database directory and run the Python script.

## Usage

Each database directory contains a Python script demonstrating data ingestion and basic similarity search using open-source embeddings. The scripts use the Sentence Transformer model for generating embeddings.

To run a script:

```
python <database_name>/<script_name>.py
```

For example:
```
python pgvector/pgvector_ingestion.py
```

Make sure to update the connection details and customize the data according to your needs.

## Vector DB Cookbook

The `vector_db_cookbook.py` script in the root directory demonstrates how to prepare data for multiple vector databases using a unified approach. It's a useful starting point for working with different vector database formats.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. Always follow best practices for security and performance when working with databases.
