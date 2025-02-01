# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

# Pydantic model to handle request bodies
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Route: Home
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Route: Get Item by Item ID
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Route: Create Item (POST)
@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price, "tax": item.tax}

# Route: Get All Items
@app.get("/items/")
def get_items():
    return [
        {"item_id": 1, "name": "Item A", "price": 25.0},
        {"item_id": 2, "name": "Item B", "price": 50.0}
    ]

