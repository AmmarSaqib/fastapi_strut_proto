"""
Author: Ammar Saqib
"""

from typing import Optional
from fastapi import APIRouter, Header, Query
from app.schemas import ModelName, Item

router = APIRouter(
    prefix="/role_templates",
    tags=['Role Templates']
)

# pylint: disable=line-too-long

@router.post("/")
def read_root():
    """
    Testing this shit
    """
    return {"Hello": "World"}

@router.get("/items/{item_id}")
def read_item(item_id: int, _q: Optional[str] = None, header: Optional[str] = Header(None), has_clients: Optional[str] = Query(Header(None), alias="hasClients")):
    """
    Testing this shit
    """
    return {"item_id": item_id, "q": _q, "header": header, "hasClients": has_clients}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    Testing this shit
    """
    return {"item_price": item.price, "item_id": item_id}

@router.get("/{model_name}")
def get_model(model_name: ModelName):
    """
    Testing this shit
    """
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
