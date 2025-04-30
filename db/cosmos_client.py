from azure.cosmos import CosmosClient

COSMOS_ENDPOINT = "https://<your-account>.documents.azure.com:443/"
COSMOS_KEY = "<your-key>"
DATABASE_ID = "<your-db-name>"

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
db = client.get_database_client(DATABASE_ID)

ticket_container = db.get_container_client("Tickets")
customer_container = db.get_container_client("Customers")
