import streamlit as st


def initialize_session():

    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "hint_level" not in st.session_state:
        st.session_state.hint_level = 1

    if "current_pattern" not in st.session_state:
        st.session_state.current_pattern = ""

    # ✅ NEW
    if "manual_question" not in st.session_state:
        st.session_state.manual_question = ""