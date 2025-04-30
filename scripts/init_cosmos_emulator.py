from azure.cosmos import CosmosClient, PartitionKey
import os
from dotenv import load_dotenv
import urllib3

# Suppress HTTPS warnings (since emulator uses self-signed cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

print("COSMOS_ENDPOINT", os.getenv("COSMOS_ENDPOINT"))
print("COSMOS_KEY", os.getenv("COSMOS_KEY"))

# ✅ Connect to Cosmos DB Emulator with cert verification disabled
client = CosmosClient(
    url=os.getenv("COSMOS_ENDPOINT"),
    credential=os.getenv("COSMOS_KEY"),
    connection_verify=False  # <--- THIS IS CRUCIAL FOR EMULATOR
)

# Create database if not exists
db = client.create_database_if_not_exists(id=os.getenv("COSMOS_DATABASE_ID"))

# Create Containers
ticket_container = db.create_container_if_not_exists(
    id=os.getenv("COSMOS_TICKET_CONTAINER"),
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)

customer_container = db.create_container_if_not_exists(
    id=os.getenv("COSMOS_CUSTOMER_CONTAINER"),
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)

# Insert Dummy Ticket Data
dummy_tickets = [
    {"id": "TICKET001", "title": "VPN Issue", "status": "Open", "customer_id": "C123"},
    {"id": "TICKET002", "title": "Email not working", "status": "Open", "customer_id": "C123"},
    {"id": "TICKET003", "title": "Laptop overheating", "status": "In Progress", "customer_id": "C456"},
    {"id": "TICKET004", "title": "Access request for Jira", "status": "Closed", "customer_id": "C456"},
    {"id": "TICKET005", "title": "Forgot password", "status": "Open", "customer_id": "C789"},
]

for ticket in dummy_tickets:
    ticket_container.upsert_item(ticket)

# Insert Dummy Customer Data
dummy_customers = [
    {"id": "C123", "name": "Alice Johnson", "email": "alice@example.com"},
    {"id": "C456", "name": "Bob Smith", "email": "bob@example.com"},
    {"id": "C789", "name": "Charlie Lee", "email": "charlie@example.com"},
]

for customer in dummy_customers:
    customer_container.upsert_item(customer)

print("✅ Cosmos Emulator initialized with dummy data.")
