from fastapi import FastAPI, Depends, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.billing import BillingManagementClient
from azure.mgmt.subscription import SubscriptionClient
from decouple import Config

config = Config()

# Access environmental values from .env file in same directory for security 
AZURE_CLIENT_ID = config("AZURE_CLIENT_ID")
AZURE_CLIENT_SECRET = config("AZURE_CLIENT_SECRET")
AZURE_TENANT_ID = config("AZURE_TENANT_ID")
AZURE_SUBSCRIPTION_ID = config("AZURE_SUBSCRIPTION_ID")
AZURE_USERNAME = config("AZURE_USERNAME")
AZURE_PASSWORD = config("AZURE_PASSWORD")

app = FastAPI()

Instrumentator().instrument(app).expose(app)

credential = DefaultAzureCredential()
subscription_id = AZURE_SUBSCRIPTION_ID

billing_client = BillingManagementClient(credential, subscription_id)
subscription_client = SubscriptionClient(credential)

# Define FastAPI routes

@app.get("/get_billing_info")
def get_billing_info():
    try:
        # Fetch billing information for the specified subscription
        invoices = billing_client.invoices.list(subscription_id)
        billing_data = [i.as_dict() for i in invoices]
        return billing_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)
















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
