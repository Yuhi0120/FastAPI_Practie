from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}/")
async def get_items(
    *,
    item_id: int = Path(title="Item's id to get", ge=2),
    q: str
):
    
# ge ... Greater equal
# gt ... Greater that
# le ... Less equal
# lt ... Less than  
    results = {"item_id": item_id}

    if q:
        results.update({"q": q})
    return results