# import statement
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# To create FastAPI app
task = FastAPI()

# In-memory data storage
data_store = []
current_id = 1

# request validation
class Item(BaseModel):     
    name: str
    price: float
    description: str | None = None


# Add new data
@task.post("/items")          #create item
def create_item(item: Item):
    global current_id

    new_item = {              
        "id": current_id,
        "name": item.name,
        "price": item.price,
        "description": item.description
    }

    data_store.append(new_item)   #assign unique id
    current_id += 1

    return {                      #new item response
        "message": "Item is created successfully",
        "item": new_item
    }


# View all data
@task.get("/items")
def get_all_items():
    return {
        "total_items": len(data_store),
        "items": data_store
    }


# View data by ID
@task.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    for item in data_store:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Item is not found"
    )