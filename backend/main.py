from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# create a request model
class UserRequest(BaseModel):
    name: str

@app.get("/hello")
async def hello():
    return {"message": "Hello, World!"}

@app.post("/greet")
async def greet(user_request: UserRequest):
    name = user_request.name
    return {"message": f"Hello, {name}!"
            f"Welcome to the fastAPI backend" }