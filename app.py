import streamlit as st


from ui import login_page, header, game


def main():
    # Initialize session state variables if they don't exist
    if "session_id" not in st.session_state:
        st.session_state.session_id = None
    if "username" not in st.session_state:
        st.session_state.username = None

    if st.session_state.session_id is None:
        login_page()
    else:
        header()
        game()

if __name__ == "__main__":
    main()
