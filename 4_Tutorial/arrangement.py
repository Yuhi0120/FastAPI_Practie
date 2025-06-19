from fastapi import FastAPI

app = FastAPI()

@app.get("/user/me")
async def user_me():
    return {"message", "me"}

@app.get("/user/{user_id}")
async def read_user(user_id: str):
    return {"message", user_id}