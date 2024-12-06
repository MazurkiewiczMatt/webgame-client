import streamlit as st

from client import logout
from ui import login_page


def main():
    # Initialize session state variables if they don't exist
    if "session_id" not in st.session_state:
        st.session_state.session_id = None
    if "username" not in st.session_state:
        st.session_state.username = None

    result = None

    st.title("Signup/Login App")

    if st.session_state.session_id is None:
        login_page()
    else:
        st.write(f"Logged in as {st.session_state.username}")
        if st.button("Logout"):
            result = logout(st.session_state.username, st.session_state.session_id)
            if result.get('status') == 'success':
                st.session_state.session_id = None
                st.session_state.username = None
            st.rerun()

if __name__ == "__main__":
    main()
