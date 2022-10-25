"""
Author: Muhammad Omer Khalil
"""
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "postgresql://"
    + environ["POSTGRES_USERNAME"]
    + ":"
    + environ["POSTGRES_PASSWORD"]
    + "@"
    + environ["POSTGRES_HOST"]
    + "/"
    + environ["POSTGRES_DATABASE"]
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    """
    Used to yield a db session.
    """
    _db = SessionLocal()
    try:
        yield _db
    finally:
        _db.close()
