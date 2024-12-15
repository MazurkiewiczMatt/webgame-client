import streamlit as st

from client import logout

def header():
    with st.container(border=True):

        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.markdown('<div style="text-align: center">Metarobotics</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div style="text-align: center">Username: {st.session_state.username}</div>', unsafe_allow_html=True)
        with col3:
            if st.button("Logout"):
                logout(st.session_state.username, st.session_state.session_id)
                st.session_state.session_id = None
                st.session_state.username = None
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
