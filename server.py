from typing import Union
import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/fetch/todos/{todoId}")
def get_todos(todoId: int):
    body = requests.get("https://jsonplaceholder.typicode.com/todos/" + str(todoId))
    return body.json()



