from app.db.database import sessionLocal
from app.db.models import ChatSession

def create_session(
        session_id
):

    db = sessionLocal()

    try:

        session = ChatSession(
            session_id=session_id,
            title="New Chat"
        )

        db.add(session)

        db.commit()

    finally:
        db.close()

def rename_session(
        session_id,
        title
):

    db = sessionLocal()

    try:

        session = (

            db.query(ChatSession)

            .filter(
                ChatSession.session_id
                ==
                session_id
            )

            .first()
        )

        if session:

            session.title = title

            db.commit()

    finally:
        db.close()

def get_sessions():

    db = sessionLocal()

    try:

        sessions = (

            db.query(
                ChatSession
            )

            .all()
        )

        return [

            {
                "session_id":
                s.session_id,

                "title":
                s.title
            }

            for s in sessions
        ]

    finally:
        db.close()