# installation
## - pip install fastapi[all] to install all its dependencies
## in linux, go to the env/bin folder and provide chmos +x to activate

from fastapi import FastAPI


backend = FastAPI() # backend is any other variable so it can be anything but generally people use this

@backend.get("/") # get is the method, / is the home root path in url
async def root():
    return {"message" : "Its running"}
    # the function can do anything but in the end it must return a json, which the frontend, for example and take up and run with it

# to test this backend setup, run the backend using
# uvicorn 1_setup:backend --reload <- where uvicorn says in file 1_setup use the "backend" variable above and keep it reloading when changes are detected to make it live
# and then test curl or use postman or thunderclient or bruno in vscode
# or open the local with port 800o to see the returned json
# curl http://127.0.0.1:8000 -v

