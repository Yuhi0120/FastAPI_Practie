from fastapi import FastAPI, status
# This "status" is veerry useful
app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}