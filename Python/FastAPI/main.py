from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str                      
    content: str
    published: bool = True          #True if no value specified
    rating: Optional[int] = None    #None or empty if no value specified. Optional value of int type, no other data type

my_posts = [
            {
                "title": "title of post 2",
                "content": "title of post 2",
                "id": 1
            },
            {
                "title": "my favorite place",
                "content": "I like japan",
                "id": 2
            }
           ]

@app.get("/")
def root():
    return {"message":"Hello, World!"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

#without defining model (Class Post is a model with parameters)
'''@app.post("/createposts")
  def create_posts(payload: dict = Body(...)):
      result = f"title: {payload['title']}, content : {payload['content']}"
      return {result}'''

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    my_posts.append(post_dict)
    return {"data":post_dict}