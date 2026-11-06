from app.db.database import sessionLocal
from app.db.models import ChatSession

db = sessionLocal()

sessions = db.query(ChatSession).all()

print("Total Sessions:", len(sessions))

for s in sessions:
    print(
        s.id,
        s.session_id,
        s.title
    )

db.close()