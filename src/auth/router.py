from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
import database, utils
from . import schemas, auth, models


router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.User)
def register(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    try:
        user = schemas.UserCreate(username=username, password=password)
    except Exception as e:
        raise HTTPException(status_code=422, detail="Bad login or password")
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    
    if user.password == user.username:
        raise HTTPException(status_code=400, detail="The password must be different from the login")

    hashed_password = utils.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    try:
        user = schemas.UserLogin(username=username, password=password)
    except Exception as e:
        raise HTTPException(status_code=422, detail="Bad login or password")
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not utils.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = auth.create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}