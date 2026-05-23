from llm_client import call_llm
from code_executor1 import run_code
from problem_recommender1 import recommend_problem
from retriever1 import retrieve_context
from conversation_memory1 import save_memory, get_memory

# ✅ NEW IMPORTS
import streamlit as st
from pattern_detector1 import detect_pattern
from hint_engine import get_hint_prompt


def detect_intent(user_input: str) -> str:

    text = user_input.lower()

    if "```" in user_input:
        return "code"

    if "recommend" in text:
        return "recommend"

    # ✅ START FLOW
    if "go raiz" in text:
        return "start"

    # ✅ NEXT HINT
    if any(x in text for x in [
        "next hint",
        "more hint",
        "next",
        "hint"
    ]):
        return "hint"

    # ✅ SOLVED
    if "solved" in text:
        return "solved"

    # ✅ FULL SOLUTION
    if any(x in text for x in [
        "show code",
        "solution",
        "give code"
    ]):
        return "solution"

    if any(x in text for x in [
        "structure",
        "format",
        "pattern"
    ]):
        return "structured"

    if any(x in text for x in [
        "hi",
        "hello",
        "hey"
    ]):
        return "chat"

    return "normal"


def run_agent(user_input: str) -> str:

    intent = detect_intent(user_input)

    # 🔧 TOOL: Run code
    if intent == "code":
        return run_code(user_input)

    # 🎯 TOOL: Recommend problem
    if intent == "recommend":
        return recommend_problem()

    # ✅ START LEARNING FLOW
    if intent == "start":

        st.session_state.hint_level = 1

        # ✅ UPLOADED QUESTIONS
        if st.session_state.questions:

            st.session_state.current_question = 0

            question = st.session_state.questions[
                st.session_state.current_question
            ]

        # ✅ MANUAL QUESTION
        else:

            question = user_input.replace(
                "go raiz",
                ""
            ).strip()

            if not question:

                return """
⚠️ No question found.

Either:
- upload PDF/TXT
OR
- paste question with Go Raiz
"""

            st.session_state.manual_question = question

        pattern = detect_pattern(question)

        st.session_state.current_pattern = pattern

        prompt = get_hint_prompt(
            question,
            1
        )

        answer = call_llm(prompt)

        return f"""
# 🧩 Problem

{question}

---

# 💡 Hint Level 1

{answer}
"""

    # ✅ NEXT HINT
    if intent == "hint":

        # ✅ UPLOAD MODE
        if st.session_state.questions:

            question = st.session_state.questions[
                st.session_state.current_question
            ]

        # ✅ MANUAL MODE
        else:

            question = st.session_state.manual_question

        st.session_state.hint_level += 1

        level = st.session_state.hint_level

        if level > 5:

            return """
✅ All hints unlocked.

Now ask:
- show code
- solution
"""

        prompt = get_hint_prompt(
            question,
            level
        )

        answer = call_llm(prompt)

        return f"""
# 💡 Hint Level {level}

{answer}
"""

    # ✅ NEXT QUESTION
    if intent == "solved":

        st.session_state.current_question += 1

        st.session_state.hint_level = 1

        if (
            st.session_state.current_question
            >= len(st.session_state.questions)
        ):

            return "🎉 You solved all uploaded questions!"

        question = st.session_state.questions[
            st.session_state.current_question
        ]

        pattern = detect_pattern(question)

        st.session_state.current_pattern = pattern

        prompt = get_hint_prompt(
            question,
            1
        )

        answer = call_llm(prompt)

        return f"""
# ✅ Next Problem

{question}

---

# 💡 Hint Level 1

{answer}
"""

    # ✅ FULL SOLUTION
    if intent == "solution":

        # ✅ UPLOAD MODE
        if st.session_state.questions:

            question = st.session_state.questions[
                st.session_state.current_question
            ]

        # ✅ MANUAL MODE
        else:

            question = st.session_state.manual_question

        context = retrieve_context(question)

        prompt = f"""
You are a DSA tutor.

REFERENCE:
{context}

QUESTION:
{question}

Give:
1. Optimized explanation
2. Time complexity
3. Python code
"""

        return call_llm(prompt)

    # 🧠 Memory
    memory = get_memory()

    history = "\n".join(
        [f"User: {m['user']}\nBot: {m['bot']}" for m in memory[-3:]]
    )

    # 📚 Context
    context = retrieve_context(user_input)

    # 🧠 Dynamic Prompt
    if intent == "chat":

        prompt = f"""
You are a friendly AI assistant.

Conversation:
{history}

User:
{user_input}

Respond naturally like ChatGPT.
"""

    elif intent == "structured":

        prompt = f"""
You are a DSA tutor.

Previous conversation:
{history}

Reference context:
{context}

User question:
{user_input}

Answer in this format:

Possible interpretation:
...

Best pattern to use:
...

Why:
...

Hint:
...

Time complexity target:
...
"""

    else:

        prompt = f"""
You are a helpful DSA tutor.

Previous conversation:
{history}

Reference context:
{context}

User question:
{user_input}

Instructions:
- Understand the user's intent.
- Explain clearly and simply.
- Give examples if needed.
- Give code ONLY if user asks.

Answer naturally.
"""

    answer = call_llm(prompt)

    save_memory(user_input, answer)

    return answer