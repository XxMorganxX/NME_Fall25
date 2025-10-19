from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Create a FastAPI instance
app: FastAPI = FastAPI(title="Simple FastAPI Server")
# app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI sample app!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created successfully!", "item": item}


# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


#uvicorn server:app --reload