from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    model_config = {
        "json_schema_extra":{
            "examples": [
                {
                    "name" : "Foo",
                    "tax": 3.2
                }
            ]
        }
    }

@app.put("/items/")
async def update_items(item: Item):
    result = {"item": item}
    return result