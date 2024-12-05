import streamlit as st
import requests
import json

# URL of the Flask server
FLASK_SERVER_URL = "https://mazurkiewicz.pythonanywhere.com"


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


# Streamlit UI
def main():
    st.title("Signup/Login App")

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
            st.json(result)


if __name__ == "__main__":
    main()
