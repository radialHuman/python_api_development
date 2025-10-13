from fastapi import FastAPI
from fastapi.params import Body


backend = FastAPI() 

@backend.get("/") 
async def root():
    return {"message" : "Its running"}

@backend.post("/createposts")
def create_posts(payload : dict = Body(...)): # to get input from body of the bruno call
    print(payload)
    return {"message" : payload["title"]}
    # check bruno's post method with this url http://127.0.0.1:8000/createposts


# @backend.post("/createposts")
# def create_posts():
#     return {"message" : "done"}
    # check bruno's post method with this url http://127.0.0.1:8000/createposts


# uvicorn 2_post:backend --reload

# problems
## 1. getting message form body is not easy
## 2. client can send any data, no validation
## 3. we must force the client to send data in a particular schema not random stuff