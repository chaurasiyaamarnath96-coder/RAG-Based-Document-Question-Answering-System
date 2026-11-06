import fitz


class PDFLoader:
    @staticmethod
    def clean_text(text: str):

        replacements = {
            "Ɵ": "ti",
            "ﬁ": "fi",
            "ﬂ": "fl",
            "ﬀ": "ff",
            "ﬃ": "ffi",
            "ﬄ": "ffl",
            "딋": "",
            "딍": "",
            "딌": "",
            "떋": "",
            "떌": "",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

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
            text = page.get_text()
            text = PDFLoader.clean_text(text)

            pages_data.append(
                {
                    "text":
                    text,

                    "page":
                    page_num + 1
                }
            )

        doc.close()

        return pages_data