from langchain_text_splitters import ( RecursiveCharacterTextSplitter)

class chunker:
    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size = 800,
            chunk_overlap = 150
        )
    )

    @staticmethod
    def create_chunks(text: str):
        return chunker.splitter.split_text(text)
