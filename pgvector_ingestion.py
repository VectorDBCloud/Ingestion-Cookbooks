import psycopg2
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Create a cursor object
cur = conn.cursor()

# Enable the pgvector extension
cur.execute("CREATE EXTENSION IF NOT EXISTS vector")

# Create a table to store documents and their embeddings
cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        content TEXT,
        embedding vector(384)
    )
""")

# Sample data
documents = [
    "This is the first document.",
    "Here's the second document.",
    "And this is the third one.",
    "Is this the fourth document?",
]

# Initialize the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for the documents
embeddings = model.encode(documents)

# Insert documents and their embeddings into the database
for doc, emb in zip(documents, embeddings):
    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (doc, emb.tolist())
    )

# Commit the changes
conn.commit()

# Perform a similarity search
query = "Which document is this?"
query_embedding = model.encode([query])[0]

cur.execute("""
    SELECT content, 1 - (embedding <=> %s) AS similarity
    FROM documents
    ORDER BY similarity DESC
    LIMIT 5
""", (query_embedding.tolist(),))

results = cur.fetchall()

print("Top 5 similar documents:")
for content, similarity in results:
    print(f"Similarity: {similarity:.4f}, Content: {content}")

# Close the cursor and connection
cur.close()
conn.close()

print("pgvector ingestion and similarity search completed successfully.")
