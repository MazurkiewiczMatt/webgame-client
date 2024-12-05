import streamlit as st
import requests
import json

# URL of the Flask server
FLASK_SERVER_URL = "https://mazurkiewicz.pythonanywhere.com"

# In-memory session storage
session_id = None
username = None

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

# Streamlit UI
def main():
    global session_id, username

    result = None

    st.title("Signup/Login App")

    if session_id is None:
        # Radio buttons to switch between signup and login
        action = st.radio("Choose action", ("Signup", "Login"))

        # Input fields for username and password
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button(action):
            if action == "Signup":
                result = signup(username, password)
                st.json(result)
            elif action == "Login":
                result = login(username, password)
                if result.get('status') == 'success':
                    session_id = result.get('session_id')
                st.json(result)
    else:
        st.write(f"Logged in as {username}")
        if st.button("Logout"):
            result = logout(username, session_id)
            if result.get('status') == 'success':
                session_id = None
                username = None
            st.json(result)

    # Clear session ID if invalid session ID error is received
    if session_id is not None:
        if result is not None:
            if result.get('status') == 'error' and 'Invalid session' in result.get('message', ''):
                session_id = None
                username = None
                st.write("Session expired. Please log in again.")

if __name__ == "__main__":
    main()
