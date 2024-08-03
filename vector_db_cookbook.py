import sys
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

def create_embeddings(documents, model_name='all-MiniLM-L6-v2'):
    try:
        model = SentenceTransformer(model_name)
        return model.encode(documents)
    except Exception as e:
        print(f"Error creating embeddings: {e}")
        sys.exit(1)

def prepare_for_database(db_type, df):
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

def main():
    try:
        # Sample data
        documents = [
            "The quick brown fox jumps over the lazy dog",
            "A journey of a thousand miles begins with a single step",
            "To be or not to be, that is the question",
            "All that glitters is not gold",
            "Where there's a will, there's a way"
        ]

        # Create document embeddings
        embeddings = create_embeddings(documents)

        # Create a DataFrame with documents and their embeddings
        df = pd.DataFrame({
            'id': range(len(documents)),
            'text': documents,
            'embedding': list(embeddings)
        })

        print("Sample of the DataFrame:")
        print(df.head())
        print("\nEmbedding shape:", embeddings.shape)

        # Example usage
        print("\nPrepared data for pgvector:")
        print(prepare_for_database('pgvector', df)[:2])

        print("\nPrepared data for Milvus:")
        milvus_data = prepare_for_database('milvus', df)
        print({k: v[:2] for k, v in milvus_data.items()})

        print("\nPrepared data for ChromaDB/Qdrant:")
        chroma_data = prepare_for_database('chromadb', df)
        print({k: v[:2] for k, v in chroma_data.items()})

        print("\nText embedding preparation completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
