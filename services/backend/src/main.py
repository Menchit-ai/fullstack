from typing import List

from fastapi import Depends, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*8080.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def hello_world():
    return "hello world !"

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/texts/{text_id}", response_model=schemas.Text)
def read_text(text_id: int, db: Session = Depends(get_db)):
    db_text = crud.get_text(db, text_id=text_id)
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text

@app.post("/users/{user_id}/texts/", response_model=schemas.Text)
def create_text_for_user(
    user_id: int, text: schemas.TextCreate, db: Session = Depends(get_db)
):
    return crud.create_user_text(db=db, text=text, user_id=user_id)

@app.post("/texts/{text_id}/human_count", response_model=schemas.Text)
def count_text_as_human(text_id: int, db: Session = Depends(get_db)):
    crud.text_is_human(db, text_id)
    return read_text(text_id,db)

@app.post("/texts/{text_id}/ai_count", response_model=schemas.Text)
def count_text_as_ai(text_id: int, db: Session = Depends(get_db)):
    crud.text_is_ai(db, text_id)
    return read_text(text_id,db)

@app.get("/texts/", response_model=List[schemas.Text])
def read_texts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    texts = crud.get_texts(db, skip=skip, limit=limit)
    return texts
