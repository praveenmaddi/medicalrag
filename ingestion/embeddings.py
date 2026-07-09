from sentence_transformers import SentenceTransformer
import numpy as np


MODEL_NAME = "BAAI/bge-base-en-v1.5"


def create_embedding_model():
    """
    Load embedding model.
    """
    return SentenceTransformer(MODEL_NAME)


def generate_embeddings(chunks):
    """
    Generate embeddings for document chunks.

    Input:
        chunks:
        [
          {
            "text": "...",
            "metadata": {...}
          }
        ]

    Output:
        numpy array of vectors
    """

    model = create_embedding_model()

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return embeddings