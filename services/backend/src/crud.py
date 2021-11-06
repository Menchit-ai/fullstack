import hashlib

from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import String

from . import models, schemas


def init_db(db: Session):
    if not db.query(models.User).filter(models.User.id == 0).first():
        db_user = models.User(id=0, email="ai", hashed_password="ai")
        db.add(db_user)
        db.commit()
    db.close()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    return db.query(models.User).order_by(models.User.id.asc()).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db.query(models.Text).filter(models.Text.owner_id == user_id).delete()
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return 1

def get_texts(db: Session):
    return db.query(models.Text).all()

def get_text(db: Session, text_id: int):
    return db.query(models.Text).filter(models.Text.id == text_id).first()

def get_texts_by_owner(db: Session, user_id: int):
    return db.query(models.Text).order_by(models.Text.id.asc()).filter(models.Text.owner_id == user_id).all()

def get_human_texts(db: Session):
    return db.query(models.Text).order_by(models.Text.id.asc()).filter(models.Text.owner_id != 0).all()

def create_user_text(db: Session, text: schemas.TextCreate, user_email: String):
    user_id = get_user_by_email(db, user_email).id
    db_text = models.Text(**text.dict(), owner_id=user_id, is_human_count=0, is_ai_count=0)
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    return db_text

def text_is_human(db: Session, text_id: int):
    text = db.query(models.Text).filter(models.Text.id == text_id).first()
    text.is_human_count += 1
    db.commit()
    return text

def text_is_ai(db: Session, text_id: int):
    text = db.query(models.Text).order_by(models.Text.id.asc()).filter(models.Text.id == text_id).first()
    text.is_ai_count += 1
    db.commit()
    return text