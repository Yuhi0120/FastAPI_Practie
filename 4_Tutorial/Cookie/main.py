# Cookie is the same as Query, Path

from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(
    ads_id: str = Cookie(default=None)
):
    return {"ads_id": ads_id}

# To get multi coockies, use pydantic like this
# This way is almost the same as Header
# class Cookies(BaseModel):
#     session_id: str
#     fatebook_tracker: str | None = None
#     googall_tracker: str | None = None
