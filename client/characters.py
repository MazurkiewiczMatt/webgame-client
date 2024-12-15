import requests

from .settings import *

def fetch_character(username, session_id):
    url = f"{FLASK_SERVER_URL}/character_sheet"
    payload = {"username": username, "session_id": session_id}
    response = requests.post(url, json=payload)
    return response.json()

def create_character(starting_point, username, session_id):
    url = f"{FLASK_SERVER_URL}/create_character"
    payload = {"starting_point": starting_point, "username": username, "session_id": session_id}
    response = requests.post(url, json=payload)
    return response.json()
