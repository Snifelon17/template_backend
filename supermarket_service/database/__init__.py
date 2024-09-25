from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing_extensions import Annotated

from supermarket_service.config import settings

DATABASE_URL = settings.database_url

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


DatabaseSession = Annotated[Session, Depends(get_db)]