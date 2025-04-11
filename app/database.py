from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

engine = create_engine(
    str(settings.DATABASE_URL),
    pool_pre_ping=True,
    pool_recycle=300
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Initialize all tables in the database
def init_db():
    from app import models  # Import models here to avoid circular imports
    Base.metadata.create_all(bind=engine)
