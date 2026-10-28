from sentence_transformers import (
    SentenceTransformer
)

class Embedder:

    model = SentenceTransformer(
        "BAAI/bge-small-en-v1.5"
    )

    @staticmethod
    def create_embedding(
        text: str
    ):
        return (
            Embedder.model.encode(
                text,
                normalize_embeddings=True).tolist()
        )