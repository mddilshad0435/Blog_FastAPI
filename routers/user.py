from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import schemas,models
from repository import user


router = APIRouter(
    prefix= "/user",
    tags= ['Users']
)



@router.post("/user/", response_model=schemas.UserResponse)
async def createUser(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get("/user/{id}", response_model=schemas.UserResponse)
async def getUser(id: int, db: Session = Depends(get_db)):
    return user.getUser(id,db)