from typing import Union, Set, List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl    # This checks if this url is valid or not automatically
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tag: Set[str] = set()
    image: Union[List[Image],None] = None

@app.put("/items/")
async def updte_item(
    item: Item
):
    result = {"item": item}
    return result