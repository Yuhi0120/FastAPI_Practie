from typing import Annotated, Literal
from fastapi import FastAPI,Query
from pydantic import BaseModel, Field

app = FastAPI()

# By defining it in pydantic, we gotta use Field
# Literal is jut literal
class FilterParams(BaseModel):
    limits: int = Field(100, gt=0, le=100),
    order_by: Literal["aa", "bb"] = "bb",
    tags: list[str] = []


@app.get("/items/")
async def read_items(
    filter_query: Annotated[FilterParams, Query()]
):
    return filter_query
    