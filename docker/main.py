from fastapi import FastAPI, Depends, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from azure.cosmos import CosmosClient

app = FastAPI()

Instrumentator().instrument(app).expose(app)


url = "https://micro.documents.azure.com:443/"
key = "ZOAU0AWAVlosG3120H49mG75sixD0ACaS5rS9JycTTLtC3hU8CK2OAZzQT62nhMrmG3ylKAkLjNPACDbN0Wdfw=="

client = CosmosClient(url, credential=key)
database = client.get_database_client("ToDoList")
container = database.get_container_client("Items")


def get_container():
    return container


@app.post("/add_item/")
async def add_item(item: dict, container=Depends(get_container)):
    container.upsert_item(item)
    return {"message": "Item added"}


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
