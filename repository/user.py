from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from hashing import Hash

def create(request: schemas.User, db: Session):
    add_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user

def getUser(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with the id {id} is not available")
        
    return user

