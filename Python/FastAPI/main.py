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

@app.get("/")
def root():
    return {"message":"Hello, World!"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

#without defining model (Class Post is a model with parameters)
'''@app.post("/createposts")
  def create_posts(payload: dict = Body(...)):
      result = f"title: {payload['title']}, content : {payload['content']}"
      return {result}'''

@app.post("/createposts")
def create_posts(new_post: Post):
    # print(new_post)
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    print(new_post.rating)
    return {"message":"post created."}
            
#pydantic usage
#title str, content str