# We can define the style of output like this

from typing import Union, Any
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

@app.get("/user/", response_model=UserOut)
async def creat_user(
    user : UserIn
) -> Any:
    return user