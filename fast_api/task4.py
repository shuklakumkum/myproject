#import library
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

# Create fastapi app
task = FastAPI(title="User CRUD API")

# user model
class User(BaseModel):
    name: str
    age: int
    email: str

# fake database
users: List[User] = []

# create user
@task.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append(user)
    return {
        "message": "User created successfully",
        "user_id": len(users) - 1
    }

# read all user
@task.get("/users", response_model=List[User], status_code=status.HTTP_200_OK)
def get_all_users():
    return users

# read single user
@task.get("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return users[user_id]

# update user
@task.put("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: User):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    users[user_id] = user
    return user

# delete user
@task.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    deleted_user = users.pop(user_id)
    return {
        "message": "User deleted successfully",
        "deleted_user": deleted_user
    }

# root endpoint
@task.get("/")
def root():
    return {"message": "FastAPI CRUD is working"}