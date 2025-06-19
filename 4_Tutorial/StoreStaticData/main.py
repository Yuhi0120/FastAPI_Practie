# To store the static data, we can put it into the URL
# We can use URL as some kind of directory like this

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# eg, we can store the data in ttp://localhost:8000/static/images/logo.png