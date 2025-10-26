from fastapi import FastAPI
import json

from pydantic import BaseModel


app = FastAPI()

GCAI_NUM_MEMBERS = 30

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!", "num_members": GCAI_NUM_MEMBERS}, 200


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}, 200

@app.get("/search")
def search(q: str = "default", limit: int = 10):
    return {"query": q, "limit": limit}, 200




class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.post("/items/")
def create_item(item: Item):
    print(f"{item.name}")
    return {"message": "Item created successfully!", "item": item}

#pip install uvicorn fastapi

#uvicorn main:app --reload