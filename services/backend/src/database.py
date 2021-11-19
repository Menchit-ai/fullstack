import os
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

POSTGRES_USER = os.environ["BACKEND_USER"]
POSTGRES_PASSWORD = os.environ["BACKEND_PASSWORD"]
POSTGRES_DB = os.environ["BACKEND_DB"]
BACKEND_DB = os.environ["BACKEND_DB"]

SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{BACKEND_DB}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
