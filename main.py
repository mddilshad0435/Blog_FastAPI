from fastapi import FastAPI
from database import engine
import models
from routers import blog, user, authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="sqlalchemy database connection")

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)





