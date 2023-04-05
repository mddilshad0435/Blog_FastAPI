from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models, schemas

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(name=request.name,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def allBlogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def getBlog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"blog with the {id} is not available"}
    return blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"blog with the id {id} is not available")

    blog.delete()
    db.commit()
    return "blog deleted successfully"

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with the id {id} is not available")

    update_data = request.dict(exclude_unset=True)
    blog.update(update_data,synchronize_session=False)
    db.commit()
    return "Updated successfully"