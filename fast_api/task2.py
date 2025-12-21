
# import libraries
from fastapi import FastAPI
from pydantic import BaseModel

# create FastAPI instance named 'task'
task = FastAPI()

# Pydantic model
class User(BaseModel):
    name: str
    age: int
    email: str

#it is used to create_user
@task.post("/create_user")
def create(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }

# To GET endpoint:Path parameter
@task.get("/user/{user_id}")
def id(user_id: int):
    return {
        "user_id": user_id,
        "message": f"User details for user {user_id}"
    }

#To GET endpoint:Query parameter
@task.get("/search")
def search(keyword: str = ""):
    return {
        "keyword": keyword,
        "message": f"Searching for '{keyword}'"
    }

# Root endpoint
@task.get("/")
def root():
    return {"message": "FastAPI is working"}
