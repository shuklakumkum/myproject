# import python library
from fastapi import FastAPI

task = FastAPI()  #It is API app

@task.get("/")    #It is the root url
def main():       #function name
  return {"message": "FastAPI is working"}  #json response

@task.get("/hello")  #another GET API endpoint
def hello():
  return {"message":"hello from FastAPI"}