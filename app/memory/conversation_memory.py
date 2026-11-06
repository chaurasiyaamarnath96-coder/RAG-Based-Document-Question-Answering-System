from app.db.database import (
    sessionmaker
)

from app.db.models import (
    ChatMessage
)
from app.db.database import sessionLocal


def add_message(
        session_id,
        role,
        content
):

    db = sessionLocal()

    try:

        message = ChatMessage(

            session_id=session_id,

            role=role,

            content=content
        )

        db.add(
            message
        )

        db.commit()

    finally:

        db.close()

def get_sessions():

    db = sessionLocal()

    try:

        sessions = (

            db.query(
                ChatMessage.session_id
            )

            .distinct()

            .all()
        )

        return [

            item[0]

            for item
            in sessions
        ]

    finally:

        db.close()

def get_history(
        session_id
):

    db = sessionLocal()

    try:

        messages = (

            db.query(
                ChatMessage
            )

            .filter(
                ChatMessage.session_id
                == session_id
            )

            .all()
        )

        history = []

        for msg in messages:

            history.append(
                {
                    "role":
                    msg.role,

                    "content":
                    msg.content
                }
            )

        return history

    finally:

        db.close()
