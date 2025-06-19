from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()

async def verify_token(x_token: str =Header()):
    if x_token != "AAAAAAAAA":
        raise HTTPException(status_code=400, detail="AAAA")

async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

# Or, u can put these 2 function directory like this
# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/", dependencies=[Depends(verify_key), Depends(verify_token)])
async def read_items():
    return 10