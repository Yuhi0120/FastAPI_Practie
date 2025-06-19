from typing import Union

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    # The header often includes "-", thus we gotta change 
    # it into "_" by using convert-underscore
    user_agent: Union[str, None] = Header(default=None, convert_underscores= False)):
    # To deal with the duplicated header, use the List
    # ~ x_token: Union[List[str], None] = Header(~)
    return {"User-Agent": user_agent}