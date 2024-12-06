import streamlit as st

from client import fetch_character

def game():
    character_response = fetch_character(st.session_state.username, st.session_state.session_id)
    if character_response.get('status') == 'success':
        character = character_response.get('character')
        st.write(character)
    elif character_response.get('message') == 'Character not found':
        st.write('Character creation')
    else:
        st.warning("Something went wrong...")