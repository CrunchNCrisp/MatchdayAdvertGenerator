import requests
from datetime import datetime, timezone
from ics import Calendar

def fetch_calendar_data(url):
    """Fetches the calendar data from the provided URL."""
    if url.startswith("webcal://"):
        url = url.replace("webcal://", "https://")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching calendar data: {e}")
        exit(1)


def get_next_event(calendar_data):
    """Parses the calendar data and finds the next event."""
    try:
        calendar = Calendar(calendar_data)
        now = datetime.now(timezone.utc)
        future_events = [event for event in calendar.events if event.begin > now]
        future_events.sort(key=lambda event: event.begin)  # Sort events by start time
        return future_events[0] if future_events else None
    except Exception as e:
        print(f"Error parsing calendar data: {e}")
        exit(1)