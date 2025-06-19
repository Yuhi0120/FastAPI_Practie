import time
from fastapi import FastAPI, Request

app = FastAPI()

# Whenever the "http" request comes, 
# it take a time of process
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # Request type ... Any types of Request
    # call_next ... just running Request and when it is over
    # return detail of the process of Request
    start = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start
    response.header["X-Process-Time"] = str(process_time)
    return response