# To accept the invalid input like aaaa-aaaa, use the alies

from typing import Union
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")):

# When I wanna set that invalid input as "not appropriate", doing like
# ~ decripted = True

    result =  {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result