import requests

from .settings import *

def signup(username, password):
    url = f"{FLASK_SERVER_URL}/signup"
    payload = {"username": username, "password": password}
    response = requests.post(url, json=payload)
    return response.json()

def login(username, password):
    url = f"{FLASK_SERVER_URL}/login"
    payload = {"username": username, "password": password}
    response = requests.post(url, json=payload)
    return response.json()

def logout(username, session_id):
    url = f"{FLASK_SERVER_URL}/logout"
    payload = {"username": username, "session_id": session_id}
    response = requests.post(url, json=payload)
    return response.json()