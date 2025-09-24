# api.py
import os, requests, datetime as dt
from dotenv import load_dotenv

BASE = "https://api.track.toggl.com/api/v9"

def get_time_entries(start: dt.datetime, end: dt.datetime):
    load_dotenv()  # .env erst hier laden
    api_key = os.getenv("TOGGL_API_KEY")
    if not api_key:
        raise ValueError("TOGGL_API_KEY nicht gefunden. Bitte .env prüfen.")

    url = f"{BASE}/me/time_entries"
    params = {
        "start_date": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end_date":   end.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    r = requests.get(url, params=params, auth=(api_key, "api_token"), timeout=30)
    r.raise_for_status()
    return r.json()
