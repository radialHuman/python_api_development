from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional

from pydantic import BaseModel # to bring in type checks

backend = FastAPI() 

# to make a pydantic class which will be a representation of the data FE will send
class Post(BaseModel):
    sno : Optional[int] = None # make this variable optional by making it none, then even if not passed by FE things will work smoothly, there wont be any error
    title : str
    published : bool = True # default value initialization
# once created/declared, ti can be used donw in the code to be used as a type

@backend.get("/") 
async def root():
    return {"message" : "Its running"}

# @backend.post("/createposts")
# def create_posts(payload : dict = Body(...)): 
#     print(payload)
#     return {"sno" : payload["sno"] , "message" : payload["title"]}
    # how will the front end know what to pass and what should be the type, so sue pytdantic
    # in this case, it passes a dict with sno  :int and message : str

@backend.post("/createposts")
def create_posts(new_post : Post): # thi pydantic class will take care of the type validation and naems of the keys
    print(type(new_post))
    # convert a pydantic model to dict
    print(type(new_post.dict()))
    return { "message" : "success"}

# if the FE doesn send a field then it will raise 422 and say value missing
# if theinput is of type string here in basemodel and an int is passed, it will still take it without error as it will be type casted