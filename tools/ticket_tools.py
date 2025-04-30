from db.cosmos_client import ticket_container

def get_ticket(ticket_id: str):
    return ticket_container.read_item(item=ticket_id, partition_key=ticket_id)

def update_ticket(ticket_id: str, updates: dict):
    ticket = ticket_container.read_item(item=ticket_id, partition_key=ticket_id)
    ticket.update(updates)
    return ticket_container.replace_item(item=ticket_id, body=ticket)

def create_ticket(data: dict):
    return ticket_container.create_item(body=data)

def add_ticket_note(ticket_id: str, note: str):
    ticket = ticket_container.read_item(item=ticket_id, partition_key=ticket_id)
    ticket.setdefault("notes", []).append(note)
    return ticket_container.replace_item(item=ticket_id, body=ticket)

def add_timelog(ticket_id: str, hours: float):
    ticket = ticket_container.read_item(item=ticket_id, partition_key=ticket_id)
    ticket.setdefault("timelogs", []).append({"hours": hours})
    return ticket_container.replace_item(item=ticket_id, body=ticket)
