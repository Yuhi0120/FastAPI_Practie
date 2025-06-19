from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    a = "a"
    b = "b"
    c = "c"

app = FastAPI()

@app.get("/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.a:
        return {"message", model_name}

    if model_name.value == "b":
        return {"message", model_name}