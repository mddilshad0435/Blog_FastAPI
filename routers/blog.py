from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import schemas,models
from repository import blog
from . import  oauth2


router = APIRouter(
    prefix= "/blog",
    tags= ['Blog']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.BlogResponse)
async def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get("/", response_model=List[schemas.BlogResponse])
async def all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.allBlogs(db)


@router.get("/{id}", response_model=schemas.BlogResponse)
async def get_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.getBlog(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id,db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

