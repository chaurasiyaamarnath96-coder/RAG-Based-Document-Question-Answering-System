import os


from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)


from app.services.ingest_service import (
    IngestService
)
router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

@router.post("")
async def upload_pdf(
    file: UploadFile = File(...),
    session_id: str =Form(...)

):
    print("UPLOAD SESSION ID:", session_id)
    save_path = (f"data/pdfs/{file.filename}")

    with open(
        save_path,
        "wb"
    ) as buffer:
        buffer.write(await file.read())
    print("UPLOAD SESSION ID:", session_id)
    results = (
        IngestService.process_pdf(
            save_path,
            file.filename,
            session_id
        )
    )
    return {
        "filename": file.filename,
        "pages": results["pages"],
        "characters": results["chars"],
        "chunks": results["chunks"]
    }
