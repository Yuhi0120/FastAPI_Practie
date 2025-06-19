from typing import Union
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token")

class User(BaseModel):
    username: str

def decode_token(token):
    return User(
        username = token + "AAA"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    return user

@app.get("/user/me")
async def read_user_me(current_user : User = Depends(get_current_user)):
    return current_user