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
            filename,
            session_id
    ):
        print("PROCESS_PDF SESSION:", session_id)
        pages_data = (
            PDFLoader.extract_text(
                pdf_path
            )
        )

        all_chunks = []

        total_chars = 0

        for page_data in pages_data:

            text = page_data["text"]

            pages = page_data["page"]
            if not text:
                continue

            total_chars += len(
                text
            )

            embeddings = (
                EmbeddingService
                .process_text(
                    text
                )
            )
            print("TEXT:", text[:100])
            EmbeddingService.process_text(text)
            print("Embeddings:", embeddings)
            for item in embeddings:

                item["pages"] = pages
                print("INGEST SESSION:", session_id)
                item["session_id"] = session_id

            all_chunks.extend(
                embeddings
            )

        store_chunks(
            all_chunks,
            filename,
            pages,
            session_id
        )

        return {

            "pages":
            len(pages_data),

            "chars":
            total_chars,

            "chunks":
            len(all_chunks),
            "session_id":"string"
        }