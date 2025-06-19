from typing import Annotated, Union
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(description="this is float")
    # We can use field as above like this
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

@app.put("/items/")
async def update_item(
    item_id: Annotated[int, Path(description="ididid")],
    item: Item,
    user: User,
    importance: int = Body() # Withoud using this, it will be treated as query, so it should 
                             # appear in the URL, not in the JSON
):
    result = {"item?id": item_id, "item": item, "user": user, "importance" : importance}
    return result

# To embeed s single body, do like this
# item: Annotated[Item, Body(embed=True)])