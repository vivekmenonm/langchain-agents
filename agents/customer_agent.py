from langchain.tools import Tool
from tools.customer_tools import (
    get_customer, update_customer, create_customer, add_contact, get_contact
)

customer_tools = [
    Tool.from_function(get_customer, name="get_customer", description="Fetch customer info by ID"),
    Tool.from_function(update_customer, name="update_customer", description="Update customer"),
    Tool.from_function(create_customer, name="create_customer", description="Create customer record"),
    Tool.from_function(add_contact, name="add_contact", description="Add contact to customer"),
    Tool.from_function(get_contact, name="get_contact", description="Get contact details by customer ID"),
]