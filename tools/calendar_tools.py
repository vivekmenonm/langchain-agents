calendar_db = []

def create_event(title: str, date: str, user: str):
    event = {"title": title, "date": date, "user": user}
    calendar_db.append(event)
    return f"Event '{title}' for {user} on {date} created."

def get_events(user: str):
    return [event for event in calendar_db if event["user"] == user]
