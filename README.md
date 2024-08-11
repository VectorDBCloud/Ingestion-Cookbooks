![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-green.svg)

# Ingestion Cookbook

This repository contains a collection of scripts for ingesting data into various vector databases using open-source embeddings. It serves as a cookbook with recipes (scripts) for advanced data ingestion techniques and similarity search.


## Table of Contents

1. [Supported Vector Databases](#supported-vector-databases)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Vector DB Cookbook](#vector-db-cookbook)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)
8. [Contribution and Feedback](#contribution-and-feedback)
9. [Related Resources](#related-resources)
10. [License](#license)
11. [Disclaimer](#disclaimer)


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

Make sure to update the connection details and customize the data according to your needs. You can modify the script parameters, input data, and embedding model to suit your specific use case.

## Vector DB Cookbook

The `vector_db_cookbook.py` script in the root directory demonstrates how to prepare data for multiple vector databases using a unified approach. It's a useful starting point for working with different vector database formats.

This script showcases:
- Data preprocessing techniques
- Embedding generation using various models
- Formatting data for different vector databases
- Basic similarity search implementation

To use the cookbook:
```
python vector_db_cookbook.py
```

## Best Practices

1. **Data Preparation**: Ensure your data is clean and properly formatted before ingestion.
2. **Embedding Selection**: Choose appropriate embedding models for your data type and use case.
3. **Batch Processing**: For large datasets, implement batch processing to avoid memory issues.
4. **Error Handling**: Implement robust error handling and logging in your ingestion scripts.
5. **Performance Optimization**: Use bulk inserts and optimize your queries for better performance.
6. **Regular Updates**: Keep your vector database and embeddings up-to-date with your latest data.
7. **Security**: Always use secure connections and API keys when working with cloud-based vector databases.

## Troubleshooting

If you encounter issues:

1. Ensure all environment variables are correctly set.
2. Check your internet connection and API endpoint accessibility.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. For specific error messages, refer to the documentation of the respective vector database or create an issue in this repository.

## Contribution and Feedback

We encourage contributions to enhance these ingestion scripts. For contributing new scripts or suggesting improvements, please refer to our [Contribution Guidelines](CONTRIBUTING.md). If you encounter issues or have suggestions, please use the issue tracker.

## Related Resources

- [Vector Database Cloud Documentation](https://docs.vectordbcloud.com)
- [Open-Source Embeddings Repository](https://github.com/VectorDBCloud/Open-Source-Embedding-Cookbook)
- [Vector Database Benchmarks](https://github.com/VectorDBCloud/Benchmarks)
- [Vector Database Use Cases](https://github.com/VectorDBCloud/Use-Cases)


## License

This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0).

Copyright (c) 2024 Vector Database Cloud

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- Attribution — You must give appropriate credit to Vector Database Cloud, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests Vector Database Cloud endorses you or your use.

Additionally, we require that any use of this guide includes visible attribution to Vector Database Cloud. This attribution should be in the form of "Ingestion Cookbooks by Vector Database Cloud" or "Based on Vector Database Cloud Ingestion Cookbooks", along with a link to https://vectordbcloud.com, in any public-facing applications, documentation, or redistributions of this guide.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full license text, visit: https://creativecommons.org/licenses/by/4.0/legalcode


## Disclaimer

The information and resources provided in this community repository are for general informational purposes only. While we strive to keep the information up-to-date and correct, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the information, products, services, or related graphics contained in this repository for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

Vector Database Cloud configurations may vary, and it's essential to consult the official documentation before implementing any solutions or suggestions found in this community repository. Always follow best practices for security and performance when working with databases and cloud services.

The content in this repository may change without notice. Users are responsible for ensuring they are using the most current version of any information or code provided.

This disclaimer applies to Vector Database Cloud, its contributors, and any third parties involved in creating, producing, or delivering the content in this repository.

The use of any information or code in this repository may carry inherent risks, including but not limited to data loss, system failures, or security vulnerabilities. Users should thoroughly test and validate any implementations in a safe environment before deploying to production systems.

For complex implementations or critical systems, we strongly recommend seeking advice from qualified professionals or consulting services.

By using this repository, you acknowledge and agree to this disclaimer. If you do not agree with any part of this disclaimer, please do not use the information or resources provided in this repository.
