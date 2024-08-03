import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Sample data
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "To be or not to be, that is the question",
    "All that glitters is not gold",
    "Where there's a will, there's a way"
]

# Initialize the sentence transformer model from Hugging Face
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create document embeddings using the Sentence Transformer model
embeddings = model.encode(documents)

# Create a DataFrame with documents and their embeddings
df = pd.DataFrame({
    'id': range(len(documents)),
    'text': documents,
    'embedding': list(embeddings)
})

print("Sample of the DataFrame:")
print(df.head())
print("\nEmbedding shape:", embeddings.shape)

# Function to prepare data for different vector databases
def prepare_for_database(db_type):
    if db_type == 'pgvector':
        return df.to_dict('records')
    elif db_type == 'milvus':
        return {
            'id': df['id'].tolist(),
            'text': df['text'].tolist(),
            'embedding': df['embedding'].tolist()
        }
    elif db_type in ['chromadb', 'qdrant']:
        return {
            'ids': df['id'].astype(str).tolist(),
            'documents': df['text'].tolist(),
            'embeddings': df['embedding'].tolist()
        }
    else:
        raise ValueError(f"Unsupported database type: {db_type}")

# Example usage
print("\nPrepared data for pgvector:")
print(prepare_for_database('pgvector')[:2])

print("\nPrepared data for Milvus:")
milvus_data = prepare_for_database('milvus')
print({k: v[:2] for k, v in milvus_data.items()})

print("\nPrepared data for ChromaDB/Qdrant:")
chroma_data = prepare_for_database('chromadb')
print({k: v[:2] for k, v in chroma_data.items()})

print("\nText embedding preparation completed successfully.")
