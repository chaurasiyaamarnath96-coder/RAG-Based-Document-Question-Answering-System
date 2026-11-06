from typing import Literal

from pydantic import (
    BaseModel,
    Field
)


class FeedbackRequest(
        BaseModel
):

    session_id: str = Field(
        min_length=1,
        max_length=100
    )

    query: str = Field(
        min_length=1
    )

    answer: str = Field(
        min_length=1
    )

    rating: Literal[
        "like",
        "dislike"
    ]