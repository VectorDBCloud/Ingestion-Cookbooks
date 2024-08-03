![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Ingestion Cookbook

This repository contains a collection of scripts for ingesting data into various vector databases using open-source embeddings. It serves as a cookbook with recipes (scripts) for advanced data ingestion techniques and similarity search.

## Table of Contents

- [Supported Vector Databases](#supported-vector-databases)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Vector DB Cookbook](#vector-db-cookbook)
- [Troubleshooting](#troubleshooting)
- [Contribution and Feedback](#contribution-and-feedback)
- [Disclaimer](#disclaimer)

## Supported Vector Databases

- [pgvector](pgvector/): PostgreSQL extension for vector similarity search
- [Milvus](milvus/): Cloud-native vector database for similarity search
- [ChromaDB](chromadb/): Open-source embedding database
- [Qdrant](qdrant/): Vector database for next-gen AI applications

## Prerequisites

- Python 3.7+
- Access to Vector Database Cloud with API URL and API key for each database
- Basic understanding of vector databases and their applications

## Installation

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

## Troubleshooting

If you encounter issues:

1. Ensure all environment variables are correctly set.
2. Check your internet connection and API endpoint accessibility.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. For specific error messages, refer to the documentation of the respective vector database or create an issue in this repository.


## Contribution and Feedback

We encourage contributions to enhance these ingestion scripts. For contributing new scripts or suggesting improvements, please refer to our [Contribution Guidelines](CONTRIBUTING.md). If you encounter issues or have suggestions, please use the issue tracker.

## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.

Vector Database Cloud configurations may vary, and it's essential to consult the official documentation and your system administrators before running these scripts in your environment. Ensure you have the necessary permissions and understand the potential impact of each operation on your data and system resources.
