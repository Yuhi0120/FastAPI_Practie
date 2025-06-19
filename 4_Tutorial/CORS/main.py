# The server accepts specific client by using url

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,             # Advocate
    allow_origins=origins,      # The list of origin
    allow_credentials=True,     # If accept cookie etc
    allow_methods=["*"],        # Which HTTP method(like GET, POST)
    allow_headers=["*"],         # which header ("Content-Type", "X-My-Header") 
)

@app.get("/")
async def main():
    return {"message": "Hello World"}