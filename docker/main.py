from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.get("/live")
def healthz():
    '''Function to check health'''
    return {"Status": "OK"}

@app.get("/ready")
def readiness():
    '''Function to check readiness'''
    return {"Status": "OK"}
