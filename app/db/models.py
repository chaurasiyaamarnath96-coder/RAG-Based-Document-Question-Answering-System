from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)

from app.db.database import(
    Base
)

class ChatMessage(
    Base
):
    __tablename__ = ("chat_message")
    id = Column(
        Integer,
        primary_key= True,
        index=True
    )
    session_id = Column(
        String,
        index=True
        )
    role = Column(
        String,
        index=True
        )
    content = Column(Text)

class Feedback(
        Base
):

    __tablename__ = "feedback"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        String
    )

    query = Column(
        Text
    )

    answer = Column(
        Text
    )

    rating = Column(
        String
    )

class ChatSession(Base):

    __tablename__ = "chat_sessions"

    id = Column(
        Integer,
        primary_key=True
    )

    session_id = Column(
        String,
        unique=True
    )

    title = Column(
        String,
        default="New chat"       
    )