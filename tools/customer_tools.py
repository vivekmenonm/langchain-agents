from db.cosmos_client import customer_container

def get_customer(customer_id: str):
    return customer_container.read_item(item=customer_id, partition_key=customer_id)

def update_customer(customer_id: str, updates: dict):
    customer = customer_container.read_item(item=customer_id, partition_key=customer_id)
    customer.update(updates)
    return customer_container.replace_item(item=customer_id, body=customer)

def create_customer(data: dict):
    return customer_container.create_item(body=data)

def add_contact(customer_id: str, contact_info: dict):
    customer = customer_container.read_item(item=customer_id, partition_key=customer_id)
    customer.setdefault("contacts", []).append(contact_info)
    return customer_container.replace_item(item=customer_id, body=customer)

def get_contact(customer_id: str):
    customer = customer_container.read_item(item=customer_id, partition_key=customer_id)
    return customer.get("contacts", [])
