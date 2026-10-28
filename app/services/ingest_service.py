from app.ingestion.pdf_loader import (
    PDFLoader
)

from app.services.embedding_service import (
    EmbeddingService
)

from app.vectordb.vector_store import (
    store_chunks
)


class IngestService:

    @staticmethod
    def process_pdf(
            pdf_path,
            filename
    ):

        pages_data = (
            PDFLoader.extract_text(
                pdf_path
            )
        )

        all_chunks = []

        total_chars = 0

        for page_data in pages_data:

            text = page_data["text"]

            page = page_data["page"]

            total_chars += len(
                text
            )

            embeddings = (
                EmbeddingService
                .process_text(
                    text
                )
            )

            for item in embeddings:

                item["page"] = page

            all_chunks.extend(
                embeddings
            )

        store_chunks(
            all_chunks,
            filename
        )

        return {

            "pages":
            len(pages_data),

            "chars":
            total_chars,

            "chunks":
            len(all_chunks)
        }