from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel

# To use "Form" just do like this

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data