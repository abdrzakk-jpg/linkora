
from app.db.database import SessionLocal


def get_db():
    """ DB-sessions controller (open&close) """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
