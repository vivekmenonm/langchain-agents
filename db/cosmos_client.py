from azure.cosmos import CosmosClient
import os
from dotenv import load_dotenv
import urllib3

load_dotenv()

# Emulator certificate is self-signed; disable verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")

client = CosmosClient(
    url=COSMOS_ENDPOINT,
    credential=COSMOS_KEY,
    connection_verify=False  # ✅ this is the key fix
)

db = client.get_database_client(os.getenv("COSMOS_DATABASE_ID"))

ticket_container = db.get_container_client(os.getenv("COSMOS_TICKET_CONTAINER"))
customer_container = db.get_container_client(os.getenv("COSMOS_CUSTOMER_CONTAINER"))