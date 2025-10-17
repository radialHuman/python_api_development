from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from typing import Optional

from pydantic import BaseModel # to bring in type checks

backend = FastAPI()  

class Post(BaseModel):
    sno : Optional[int] = None 
    title : str
    published : bool = True 

@backend.get("/") 
async def root():
    return {"message" : "Its running"}


# @backend.post("/createposts")
# def create_posts(new_post : Post):
#     print(type(new_post))
#     print(type(new_post.dict()))
#     return { "message" : "success"}

# CRUD operation api best practices
# for any post function, it should be like this and not like the above one
# always have them in plural : posts, create_users
# create : @app.post("/posts")
# reads specific : @app.get("/posts/{id}") 
# read all : @app.get("/posts")
# update : @app.put("/posts/{id}")
# delete : @app.delete("/posts/{id}")

# the default succss status code is 200 but to change that do the following in the deocrator

@backend.post("/posts/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(new_post : Post):
    print(type(new_post))
    print(type(new_post.dict()))
    return { "message" : "success"}

# retreiving one post
# @backend.get("/post/{id}") # this si a path parameter which will be embedded from frontend input
# def get_post(id : int):
#     print(id)
#     return {"message" : 'post # {} retrieved'.format(id)}

# route order matters, the one that comes first will be taken by fastapi
# if there is another route below with .get("/posts/latest"), this wont work as the previous one will be taken
# also it would assume id here is latest 


## http status codes must be used  while returning to FE not just null if anything is not found in BE
# 200 OK : successful
# 404 : not found
# 201 Created : somethign was created
# 500 : server error

some_data = {1: "x"}

def find_post(id : int):
    if id in some_data.keys():
        print(some_data[id])
        return some_data[id]
    else:
        return None

# @backend.get("/post/{id}") # this si a path parameter which will be embedded from frontend input
def get_post(id : int, response: Response): # from Fastapi import
    post = find_post(id)
    if post == None : # to check for null
        response.status_code = 404
        # a better way of doing this is using status, imported from fastapi
        response.status_code = status.HTTP_404_NOT_FOUND

        return {"error" : response.status_code}
    else:
        print(id)
        return {"message" : 'post # {} retrieved'.format(id)}


# even better is to use a exception raising using HTTPException

@backend.get("/post/{id}") # this si a path parameter which will be embedded from frontend input
def get_post(id : int, response: Response): # from Fastapi import
    post = find_post(id)
    if post == None : # to check for null
        # response.status_code = 404
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {id} not found")

        return {"error" : response.status_code}
    else:
        print(id)
        return {"message" : 'post # {} retrieved'.format(id)}