from app.db.database import (
    sessionLocal
)

from app.db.models import (
    Feedback
)

def save_feedback(
        session_id,
        query,
        answer,
        rating
):

    db = sessionLocal()

    try:

        item = Feedback(

            session_id=
            session_id,

            query=
            query,

            answer=
            answer,

            rating=
            rating
        )

        db.add(
            item
        )

        db.commit()

    finally:

        db.close()


def feedback_stats():

    db = sessionLocal()

    try:

        likes = (

            db.query(
                Feedback
            )

            .filter(
                Feedback.rating
                ==
                "like"
            )

            .count()
        )

        dislikes = (

            db.query(
                Feedback
            )

            .filter(
                Feedback.rating
                ==
                "dislike"
            )

            .count()
        )

        return {

            "likes":
            likes,

            "dislikes":
            dislikes
        }

    finally:

        db.close()