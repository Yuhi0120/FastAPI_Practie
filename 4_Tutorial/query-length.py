from typing import Union
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def read_items(q: Union[str, None] = Query(default = None, min_length=3 ,max_length = 50)):
# If the str is necessary, I can do like this
# ~ (q: str = Query(..., min_length = 3))

# To define multiple variable, we can use the List like this
# ~ (q: Union[List[str], None] = Query(["apple", "foo"]))
# URL is like this  ""http://localhost:8000/items/?q=foo&q=bar"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results