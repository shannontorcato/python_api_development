from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import random, randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post 1", "content":"content of post 1", "id":1}, {"title":"title of post 2", "content":"content of post 2", "id":2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/")
async def root():
    return {"message": "Hello, welcome to Billys World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    new_post = post.dict()
    new_post['id'] = randrange(1,100000)
    my_posts.append(new_post)
    return {"data": post}
# title str, content str

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
    return {"post_detail": post}