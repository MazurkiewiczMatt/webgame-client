import requests

from .settings import *

def fetch_character(username, session_id):
    url = f"{FLASK_SERVER_URL}/character_sheet"
    payload = {"username": username, "session_id": session_id}
    response = requests.post(url, json=payload)
    return response.json()