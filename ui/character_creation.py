import streamlit as st
from client import create_character, fetch_character


def character_creation():
    st.write('Character creation:')

    col1, col2 = st.columns([1,2])

    with col1:
        with st.container(border=True):
            starting_point = st.radio("Starting point", ["University", "Corporation", "Private Venture"])
    with col2:
        with st.container(border=True):
            if starting_point == "University":
                st.markdown("### University")
                st.markdown("Starting assets:  \n"
                            "1. 200 ML expertise;   \n"
                            "2. \$20M;   \n"
                            "3. \$8M/turn university funding")
            elif starting_point == "Corporation":
                st.markdown("### Corporation")
                st.markdown("Starting assets:  \n"
                            "1. 150 ML expertise;   \n"
                            "2. \$2B;")
            elif starting_point == "Private Venture":
                st.markdown("### Private Venture")
                st.markdown("Starting assets:  \n"
                            "1. \$200M;   \n"
                            "2. \$1M/turn private funding")
            else:
                st.markdown("### Select the starting point")

    if starting_point in ("University", "Corporation", "Private Venture"):
        if st.button("Submit"):
            response = create_character(starting_point, st.session_state.username, st.session_state.session_id)
            if response.get('status') == 'success':
                st.session_state.character = fetch_character(st.session_state.username, st.session_state.session_id)
                st.rerun()
            else:
                st.warning(response.get('message'))



