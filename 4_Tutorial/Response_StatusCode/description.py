from typing import Set, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()

@app.post("/items/",
          summary="Create an Item",
          # deprecated = True    # By usin this, it is gonna ne
          # marked as deprecated
          response_description="The created Item",
          dependencies="This is description so I can write some long things"       
          )
async def create_items(item: Item):
    """
    This is docssting

    -**first**: aaaaa
    -**Second**: iiii
    """
    return item