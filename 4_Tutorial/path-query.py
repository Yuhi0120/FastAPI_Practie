from typing import Union
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(title="The id of the item to get"),
    q: Union[str, None] = Query(None, alias="item-query")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    
    return results