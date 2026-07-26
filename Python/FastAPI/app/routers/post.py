from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/posts",  # This will prefix all routes in this router with /posts
    tags=["Posts"]  # This will categorize the routes under "posts" in the API documentation
)

# we are using / here because we are using prefix="/posts" in the router
# remember that this will append /posts to all the post api calls 
# when the router is included in the main app

# get all posts
@router.get("/")
def get_posts(db: Session = Depends(get_db), response_model=schemas.PostResponse):
    # this will return all posts from the database
    # db.query(models.Post) - this is similar to SELECT * FROM posts
    # .all() - this will return all rows from the query
    all_posts = db.query(models.Post).all()
    return all_posts

# create a new post, also change the status to 201 when success
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())  # this will create a new post object
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    db.add(new_post)  # this will add the post to the database
    db.commit()
    db.refresh(new_post)  # this will refresh the post object with the new data from the database
    # db.refresh is used to get the id of the new post
    return new_post


# get post by id
@router.get("/{id}")
def get_post(id: int, db: Session = Depends(get_db), response_model=schemas.PostResponse):
    # this will return the first post with the given id
    # .first() will return None if no post is found with the given id
    current_post = db.query(models.Post).filter(models.Post.id == id).first() #adding first or all is important, otherwise it will return a query object
    # if current_post is None, it means that no post was found with the given id
    # if post does not exist, send 404 and error message
    if not current_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return current_post


# delete post
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_post(id: int, db: Session = Depends(get_db)):
    deleted_post = db.query(models.Post).filter(models.Post.id == id).delete()  # this will delete the post with the given id
    print(deleted_post)
    db.commit()  # this will commit the changes to the database 
    if deleted_post == 0 or deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist or is already deleted.")
    return Response(status_code=status.HTTP_200_OK)


# update post by id and post (of type Post which is a Model)
@router.put("/{id}")
def update_posts(id: int, post: schemas.Post, db: Session = Depends(get_db), response_model=schemas.PostResponse):
    # this will update the post with the given id
    # .filter(models.Post.id == id) - this will filter the posts by id
    updated_post_query = db.query(models.Post).filter(models.Post.id == id)

    updated_post = updated_post_query.first()
    if updated_post == 0 or update_posts == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Post with id: {id} does not exist.")

    updated_post_query.update(post.model_dump())  # this will update the post with the new data
    db.commit()
    
    return updated_post_query.first()  # return the updated post