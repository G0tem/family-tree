from fastapi import APIRouter, HTTPException
from schemas.MangoSchemas import Item
from database import collection
from bson import ObjectId


mango_router = APIRouter(prefix="/api/v1", tags=["Mango"])


@mango_router.post("/items/", response_model=Item)
def create_item(item: Item):
    """Create item

    Args:
        item (Item): Item model

    Returns:
        _type_: Item model save
    """
    item_dict = item.dict()
    result = collection.insert_one(item_dict)
    item_dict["id"] = str(result.inserted_id)
    print(item_dict["id"])
    return item_dict


@mango_router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):
    """Get item

    Args:
        item_id (str): str id item in db

    Raises:
        HTTPException: 404 not found

    Returns:
        _type_: item from MangoDB
    """
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item["id"] = str(item.pop("_id"))
    return item


@mango_router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, item: Item):
    """Update item

    Args:
        item_id (str): str id item in db
        item (Item): Item model

    Raises:
        HTTPException: 404 not found

    Returns:
        _type_: Uptate item result
    """
    item_dict = item.dict()
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = collection.find_one({"_id": ObjectId(item_id)})
    updated_item["id"] = str(updated_item.pop("_id"))
    return updated_item


@mango_router.delete("/items/{item_id}")
def delete_item(item_id: str):
    """Delete item

    Args:
        item_id (str): item id

    Raises:
        HTTPException: 404 not found

    Returns:
        _type_: dict result delete
    """
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
