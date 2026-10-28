from pydantic import BaseModel

class UploadResponse(BaseModel):
    filename: str
    pages : int
    extracted_chars:int