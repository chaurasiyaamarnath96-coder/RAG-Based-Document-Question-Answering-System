import fitz


class PDFLoader:

    @staticmethod
    def extract_text(
            pdf_path: str
    ):

        doc = fitz.open(
            pdf_path
        )

        pages_data = []

        for page_num, page in enumerate(
                doc
        ):

            pages_data.append(
                {
                    "text":
                    page.get_text(),

                    "page":
                    page_num + 1
                }
            )

        doc.close()

        return pages_data