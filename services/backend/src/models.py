from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    texts = relationship("Text", back_populates="owner")


class Text(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    is_human_count = Column(Integer, index=True, default=0)
    is_ai_count = Column(Integer, index=True, default=0)

    owner = relationship("User", back_populates="texts")
