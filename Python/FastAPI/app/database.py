### this file is to establish connection with the postgres database

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# this is the format for postgresql
# SQLALCHEMY_DATABASE_URL = 'postgresql://username:password@hostname/database'

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/fastapi'

# establishes connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#creates a session to the database. each session is a workspace
# where you can perform operations/transactions on the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
# this is used to create the tables in the database
Base = declarative_base()

# get session to database. this will create
# session every time the database is connected
# or interacted with.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()