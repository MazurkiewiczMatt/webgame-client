import streamlit as st

from client import fetch_character

from .character_creation import character_creation

def game():
    st.session_state.character = fetch_character(st.session_state.username, st.session_state.session_id)
    if st.session_state.character.get('status') == 'success':
        character = st.session_state.character.get('character')
        st.write(character)
    elif st.session_state.character.get('message') == 'Character not found':
        character_creation()
    else:
        st.warning("Something went wrong...")