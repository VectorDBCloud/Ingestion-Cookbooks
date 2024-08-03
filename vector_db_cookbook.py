import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Sample data
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "To be or not to be, that is the question",
    "All that glitters is not gold",
    "Where there's a will, there's a way"
]

# Create document embeddings using TF-IDF
vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(documents).toarray()

# Create a DataFrame with documents and their embeddings
df = pd.DataFrame({
    'id': range(len(documents)),
    'text': documents,
    'embedding': list(embeddings)
})

print(df.head())
print("\nEmbedding shape:", embeddings.shape)
