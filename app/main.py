from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base
from app.models import User
from app.schemas import UserIn, UserOut
from app.dependencies import get_db

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut(**user.__dict__)


@app.post("/users", response_model=UserOut)
async def create_user(user: UserIn, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.name == user.name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Name already exists")

    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserOut(**db_user.__dict__)
