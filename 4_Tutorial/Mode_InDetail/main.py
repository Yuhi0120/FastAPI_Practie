# In here, I am gonna make the password enorypt code

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserBase(BaseModel):
    user_name: str

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass
    

class UserInDB(UserOut):
    hashed_password: str

def hasher(raw: str):
    hashed = raw+ "hahahaha"
    return hashed

def saver(user: UserIn):
    hashed = hasher(user.password)
    db = UserInDB(**user.dict(), hashed_password=hashed)
    return db

@app.pust("/user/", response_model = UserOut)
async def creat_user(
    user_in: UserIn
):
    user_saved = saver(user_in)
    return user_saved
