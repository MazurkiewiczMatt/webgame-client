import streamlit as st

from client import login, signup

def login_page():
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
                st.session_state.session_id = result.get('session_id')
                st.session_state.username = username
                st.rerun()
            st.json(result)