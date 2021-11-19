from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from keycloak import KeycloakOpenID
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

# launch initialisation for kong and keycloak
from . import init_kong_keycloak

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

crud.init_db(SessionLocal())

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                                 client_id="backend",
                                 realm_name="fullstack",
                                 client_secret_key="97e13e2d-90e6-447f-9e3b-914b27653821")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api")
def hello_world():
    return "Welcome on our site, AI or Human ?"

@app.post("/api/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/api/del_users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="This user does not exist")
    return crud.delete_user(db=db, user_id=user_id)

@app.get("/api/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.get("/api/texts/", response_model=List[schemas.Text])
def read_texts(db: Session = Depends(get_db)):
    texts = crud.get_texts(db)
    return texts

@app.get("/api/users/{user_email}", response_model=schemas.User)
def read_user(user_email, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/api/texts/{text_id}", response_model=schemas.Text)
def read_text(text_id: int, db: Session = Depends(get_db)):
    db_text = crud.get_text(db, text_id=text_id)
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text

@app.post("/api/users/{user_email}/texts/{pwd}", response_model=schemas.Text)
def create_text_for_user(user_email, pwd, text: schemas.TextCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    text = crud.create_user_text(db=db, text=text, user_email=user_email, user_pwd=pwd)
    if text == -1 : raise HTTPException(status_code=401, detail="Bad password")
    return text

@app.post("/api/texts/{text_id}/human_count", response_model=schemas.Text)
def count_text_as_human(text_id: int, db: Session = Depends(get_db)):
    crud.text_is_human(db, text_id)
    return read_text(text_id,db)

@app.post("/api/texts/{text_id}/ai_count", response_model=schemas.Text)
def count_text_as_ai(text_id: int, db: Session = Depends(get_db)):
    crud.text_is_ai(db, text_id)
    return read_text(text_id,db)
