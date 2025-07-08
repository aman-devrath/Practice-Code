from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

# create instance of FastAPI
app = FastAPI()

# using pydantic, we create model of the API
class Post(BaseModel):
    title: str                      
    content: str
    published: bool = True          # True if no value specified
    rating: Optional[int] = None    # None or empty if no value specified. Optional value of int type, no other data type

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

# home page
@app.get("/")
def root():
    return {"message":"Hello, World!"}


# get all posts
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * from posts""")
    all_posts = cursor.fetchall()
    return {"data":all_posts}

# create a new post, also change the status to 201 when success
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


# get post by id
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(""" SELECT * from posts where id = %s """, str(id))
    current_post = cursor.fetchone()
    ### if post does not exist, send 404 and error message
    if not current_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return current_post


# delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(""" DELETE from posts where id = %s returning *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist.")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# update post by id and post (of type Post which is a Model)
@app.put("/posts/{id}")
def update_posts(id: int, post: Post):
    cursor.execute(""" UPDATE posts set title = %s, content = %s, published = %s where id = %s returning *""", (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist.")
    return {"data": updated_post}