### this is to create/store models

from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text
from sqlalchemy.sql.expression import null
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    # we are using server_default to set default value for published column
    # if no value is specified, it will be set to True
    # also note that the True is a text value, nto a boolean value.
    published = Column(Boolean, server_default='TRUE', nullable=False)
    # created_at is a timestamp column that will be set to the current time
    # when a new post is created. It is set to not nullable.
    # now() is a function that returns the current time
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))

class User(Base):
    __tablename__ = "users"

    id=  Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))