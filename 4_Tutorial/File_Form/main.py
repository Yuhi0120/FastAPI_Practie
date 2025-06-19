from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(
    file: bytes = File(),
    fileb: UploadFile = File(),
    token: str = Form()
):
    return{
        "size": len(file),
        "token": token,
    }