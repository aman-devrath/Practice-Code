from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine
from .routers import post, user, auth

# Create the database tables
# This will create the tables in the database based on the models defined in models.py
models.Base.metadata.create_all(bind=engine)

# create instance of FastAPI
app = FastAPI()

try:
    conn = psycopg2.connect(
        host="localhost",
        database="fastapi",
        user="postgres",
        password="root",
        cursor_factory=RealDictCursor # this is used to get column names of the table
    )
    cursor = conn.cursor()
    print("Database was connected successfully")
except Exception as error:
    print("Conntecting to database failed")
    print("Erorr: ", error)

# Include routers for posts and users
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# home page
@app.get("/")
def root():
    return {"message":"Hello, World!"}