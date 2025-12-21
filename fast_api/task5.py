#import
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from typing import List
import requests

# create fastapi app
task = FastAPI(title="erro handling & validation API")

#pydantic model
class User(BaseModel):
    name: str = Field(
        ..., 
        min_length=3, 
        description="name must be 3 characters"
    )
    age: int = Field(
        ..., 
        greater=0, 
        less=120, 
        description="age must be between 1 and 119"
    )
    email: str

    @validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("email must contain '@'")
        return value

#fake database
users: List[User] = []

#create user
@task.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    try:
        users.append(user)
        return {
            "message": "user created successfully",
            "user": user
        }
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="internal server error"
        )


#get all user
@task.get("/users")
def get_users():
    if not users:
        raise HTTPException(
            status_code=404,
            detail="no user found"
        )
    return users

#get user by index
@task.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        return users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )


#delete user
@task.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        deleted_user = users.pop(user_id)
        return {
            "message": "user deleted successfully",
            "user": deleted_user
        }
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )


# try-except 
@task.get("/divide")
def divide_numbers(a: int, b: int):
    try:
        result = a / b
        return {"result": result}
    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail="division by zero is not allowed"
        )

# external API handling
@task.get("/external-api")
def call_external_api():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=504,
            detail="external API timeout"
        )
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="external API failed"
        )

# root endpoint
@task.get("/")
def root():
    return {"message": "FastAPI error handling & validation API is running"}
