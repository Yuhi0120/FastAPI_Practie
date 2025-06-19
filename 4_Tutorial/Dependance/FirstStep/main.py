from typing import Union

from fastapi import Depends, FastAPI

app = FastAPI()

async def commom_param(
    q: Union[str, None] = None,
    skip: int = 0,
    limit: int = 0
):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(common: dict = Depends(commom_param)):
    return common
@app.get("/user/")
async def read_users(common: dict = Depends(commom_param)):
    return common
