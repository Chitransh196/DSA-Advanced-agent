import streamlit as st
from orchestrator import run_agent
from conversation_memory import clear_memory

# ✅ NEW IMPORTS
from document_parser import parse_uploaded_file
from question_extractor import extract_questions
from question_manager import sort_questions_by_difficulty
from student_session import initialize_session

# --------- Page Config ---------
st.set_page_config(
    page_title="DSA Agent Raiz",
    page_icon="🤖",
    layout="centered"
)

# ✅ INIT SESSION
initialize_session()

# --------- Custom CSS (Blue + Silver + Tribal Background) ---------
st.markdown("""
<style>

/* Main background with tribal design */
.stApp {
    background: linear-gradient(rgba(11,31,58,0.90), rgba(11,31,58,0.95)),
                url("https://images.unsplash.com/photo-1549887534-1541e9326642");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #E5E7EB;
}

/* Title styling */
h1 {
    color: #60A5FA;
    text-align: center;
}

/* Subtitle */
.stCaption {
    text-align: center;
    color: #9CA3AF;
}

/* Chat bubbles */
.stChatMessage {
    border-radius: 12px;
    padding: 10px;
    backdrop-filter: blur(6px);
}

/* User message */
[data-testid="stChatMessage-user"] {
    background-color: rgba(30, 58, 95, 0.85);
}

/* Assistant message */
[data-testid="stChatMessage-assistant"] {
    background-color: rgba(46, 46, 46, 0.85);
}

/* Chat input */
.stChatInput input {
    background-color: rgba(31, 41, 55, 0.9);
    color: #E5E7EB;
}

/* Buttons */
.stButton button {
    background-color: #3B82F6;
    color: white;
    border-radius: 8px;
    border: none;
}

/* Button hover */
.stButton button:hover {
    background-color: #2563EB;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #3B82F6;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --------- Title ---------
st.title("🤖 DSA Agent Raiz")
st.caption("Ask DSA questions, get hints, run code, or request problems 🚀")

# --------- Clear Memory Button ---------
col1, col2 = st.columns([1, 5])

with col1:

    if st.button("🧹 Clear"):

        clear_memory()

        # ✅ RESET SESSION
        st.session_state.questions = []
        st.session_state.current_question = 0
        st.session_state.hint_level = 1

        st.success("Memory cleared!")

# ✅ FILE UPLOAD FEATURE
uploaded_file = st.file_uploader(
    "Upload DSA Questions PDF/TXT",
    type=["pdf", "txt"]
)

if uploaded_file:

    content = parse_uploaded_file(uploaded_file)

    questions = extract_questions(content)

    questions = sort_questions_by_difficulty(questions)

    st.session_state.questions = questions

    st.success(
        f"✅ {len(questions)} questions loaded successfully!"
    )

# --------- Chat State ---------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------- Display Previous Messages ---------
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --------- Chat Input ---------
user_input = st.chat_input("Ask your question...")

if user_input:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    with st.spinner("Thinking..."):

        response = run_agent(user_input)

    # Show assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)