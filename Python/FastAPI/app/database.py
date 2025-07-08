### this file is to establish connection with the postgres database

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# this is the format for postgresql
# SQLALCHEMY_DATABASE_URL = 'postgresql://username:password@hostname/database'

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/fastapi'

# establishes connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()