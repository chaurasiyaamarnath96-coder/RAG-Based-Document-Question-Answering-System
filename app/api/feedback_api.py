from fastapi import (
    APIRouter
)

from app.services.feedback_service import (
    save_feedback,
    feedback_stats
)

from app.schemas.feedback_schema import (
    FeedbackRequest
)

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)

@router.post("/")
def add_feedback(
    feedback: FeedbackRequest
        
):
    save_feedback(
        feedback.session_id,
        feedback.query,
        feedback.query,
        feedback.rating
    )
    return {
        "message": "feedback saved"
    }

@router.get("/stats")
def stats():

    return (
        feedback_stats()
    )