from app.ingestion.chunker import chunker

from app.ingestion.embedder import Embedder

class EmbeddingService:

    @staticmethod
    def process_text(
        text: str
    ):

        chunks = (chunker.create_chunks(text))
        results = []
        for chunk in chunks:

            vector = (
                Embedder.create_embedding(chunk)
            )
            results.append(
                {
                    "text": chunk,
                    "embedding":vector
                }
            )
            return results
