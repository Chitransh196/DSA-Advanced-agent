# from llm_client import call_llm
# from code_executor1 import run_code
# from problem_recommender1 import recommend_problem
# from retriever1 import retrieve_context
# from conversation_memory1 import save_memory, get_memory
# from pattern_detector1 import detect_pattern
# from hint_engine import get_hint_prompt


# def run_agent(
#     user_input,
#     session_data
# ):

#     text = user_input.lower().strip()

#     # ======================================
#     # SESSION INIT
#     # ======================================

#     if "questions" not in session_data:
#         session_data["questions"] = []

#     if "current_question" not in session_data:
#         session_data["current_question"] = 0

#     if "hint_level" not in session_data:
#         session_data["hint_level"] = 0

#     if "manual_question" not in session_data:
#         session_data["manual_question"] = ""

#     if "active_question" not in session_data:
#         session_data["active_question"] = ""

#     if "current_pattern" not in session_data:
#         session_data["current_pattern"] = ""
    
#     if "awaiting_question" not in session_data:
#         session_data["awaiting_question"] = False

#     # ======================================
#     # CODE REVIEW
#     # ======================================

#     if "```" in user_input:

#         return run_code(user_input)

#     # ======================================
#     # RECOMMEND
#     # ======================================

#     if "recommend" in text:

#         return recommend_problem()

#     # ======================================
#     # START RAIZ
#     # ======================================

#     if "go raiz" in text:

#         # RESET
#         session_data["hint_level"] = 1

#         # ======================================
#         # QUESTION FROM FILE
#         # ======================================

#         if session_data["questions"]:

#             question = session_data[
#                 "questions"
#             ][
#                 session_data[
#                     "current_question"
#                 ]
#             ]

#         # ======================================
#         # MANUAL QUESTION
#         # ======================================

#         else:

#             question = user_input.replace(
#                 "go raiz",
#                 ""
#             ).strip()

#             if not question:

#                 return """
# ⚠️ No question found.

# Usage:

# go raiz <paste question>

# OR upload a txt/pdf file first.
# """

#             session_data[
#                 "manual_question"
#             ] = question

#         # SAVE ACTIVE QUESTION
#         session_data[
#             "active_question"
#         ] = question

#         # DETECT PATTERN
#         pattern = detect_pattern(
#             question
#         )

#         session_data[
#             "current_pattern"
#         ] = pattern

#         # HINT LEVEL 1
#         prompt = get_hint_prompt(
#             question,
#             1
#         )

#         answer = call_llm(prompt)

#         return f"""
# # 🧩 Problem Started

# ## Hint Level: 1/5

# {answer}
# """

#     # ======================================
#     # NEXT HINT
#     # ======================================

#     if any(x in text for x in [
#         "hint",
#         "next",
#         "more"
#     ]):

#         if not session_data[
#             "active_question"
#         ]:

#             return """
# ⚠️ No active problem.

# Start with:
# go raiz <question>

# OR upload a file first.
# """

#         # LIMIT
#         if session_data[
#             "hint_level"
#         ] >= 5:

#             return """
# ✅ Maximum hint level reached.

# Now ask:
# - show code
# - solution
# """

#         # NEXT LEVEL
#         session_data[
#             "hint_level"
#         ] += 1

#         level = session_data[
#             "hint_level"
#         ]

#         question = session_data[
#             "active_question"
#         ]

#         prompt = get_hint_prompt(
#             question,
#             level
#         )

#         answer = call_llm(prompt)

#         return f"""
# # 💡 Hint Level: {level}/5

# {answer}
# """

#     # ======================================
#     # FULL SOLUTION
#     # ======================================

#     if any(x in text for x in [
#         "show code",
#         "solution",
#         "full code"
#     ]):

#         if not session_data[
#             "active_question"
#         ]:

#             return """
# ⚠️ No active problem.
# """

#         question = session_data[
#             "active_question"
#         ]

#         context = retrieve_context(
#             question
#         )

#         prompt = f"""
# You are Raiz AI.

# QUESTION:
# {question}

# REFERENCE:
# {context}

# Now provide:

# 1. Optimal explanation
# 2. Time complexity
# 3. Space complexity
# 4. Full Python solution
# """

#         return call_llm(prompt)

#     # ======================================
#     # SOLVED
#     # ======================================

#     if "solved" in text:

#         session_data[
#             "hint_level"
#         ] = 0

#         # ======================================
#         # NEXT QUESTION
#         # ======================================

#         if session_data["questions"]:

#             session_data[
#                 "current_question"
#             ] += 1

#             if (
#                 session_data[
#                     "current_question"
#                 ] >=
#                 len(
#                     session_data[
#                         "questions"
#                     ]
#                 )
#             ):

#                 return """
# 🎉 All questions solved!
# """

#             next_q = session_data[
#                 "questions"
#             ][
#                 session_data[
#                     "current_question"
#                 ]
#             ]

#             session_data[
#                 "active_question"
#             ] = next_q

#             session_data[
#                 "hint_level"
#             ] = 1

#             pattern = detect_pattern(
#                 next_q
#             )

#             session_data[
#                 "current_pattern"
#             ] = pattern

#             prompt = get_hint_prompt(
#                 next_q,
#                 1
#             )

#             answer = call_llm(prompt)

#             return f"""
# # ✅ Next Problem

# ## Hint Level: 1/5

# {answer}
# """

#         return """
# 🎉 Problem completed!
# """

#     # ======================================
#     # NORMAL CHAT
#     # ======================================

#     memory = get_memory()

#     history = "\n".join(
#         [
#             f"User: {m['user']}\nBot: {m['bot']}"
#             for m in memory[-3:]
#         ]
#     )

#     context = retrieve_context(
#         user_input
#     )

#     prompt = f"""
# You are Raiz AI DSA Mentor.

# Conversation History:
# {history}

# REFERENCE:
# {context}

# QUESTION:
# {user_input}

# Rules:
# - concise answer
# - mentorship style
# - avoid long explanations
# """

#     answer = call_llm(prompt)

#     save_memory(
#         user_input,
#         answer
#     )

#     return answer







from llm_client import call_llm
from code_executor1 import run_code
from problem_recommender1 import recommend_problem
from retriever1 import retrieve_context
from conversation_memory1 import save_memory, get_memory
from pattern_detector1 import detect_pattern
from hint_engine import get_hint_prompt


def run_agent(
    user_input,
    session_data
):

    text = user_input.lower().strip()

    # ======================================
    # SESSION INIT
    # ======================================

    if "questions" not in session_data:
        session_data["questions"] = []

    if "current_question" not in session_data:
        session_data["current_question"] = 0

    if "hint_level" not in session_data:
        session_data["hint_level"] = 0

    if "manual_question" not in session_data:
        session_data["manual_question"] = ""

    if "active_question" not in session_data:
        session_data["active_question"] = ""

    if "current_pattern" not in session_data:
        session_data["current_pattern"] = ""

    if "awaiting_question" not in session_data:
        session_data["awaiting_question"] = False

    # ======================================
    # CODE REVIEW
    # ======================================

    if "```" in user_input:

        return run_code(user_input)

    # ======================================
    # RECOMMEND
    # ======================================

    if "recommend" in text:

        return recommend_problem()

    # ======================================
    # START RAIZ
    # ======================================

    if "go raiz" in text:

        session_data["hint_level"] = 1

        manual_question = user_input.replace(
            "go raiz",
            ""
        ).strip()

        # ======================================
        # USER DIRECTLY PASTED QUESTION
        # ======================================

        if manual_question:

            question = manual_question

            session_data[
                "manual_question"
            ] = question

            session_data[
                "active_question"
            ] = question

            session_data[
                "awaiting_question"
            ] = False

        # ======================================
        # QUESTION FROM UPLOADED FILE
        # ======================================

        elif session_data["questions"]:

            question = session_data[
                "questions"
            ][
                session_data[
                    "current_question"
                ]
            ]

            session_data[
                "active_question"
            ] = question

            session_data[
                "awaiting_question"
            ] = False

        # ======================================
        # ASK USER FOR QUESTION
        # ======================================

        else:

            session_data[
                "awaiting_question"
            ] = True

            return """
🧩 Paste your DSA problem now.
"""

        # ======================================
        # DETECT PATTERN
        # ======================================

        pattern = detect_pattern(
            question
        )

        session_data[
            "current_pattern"
        ] = pattern

        # ======================================
        # LEVEL 1 HINT
        # ======================================

        prompt = get_hint_prompt(
            question,
            1
        )

        answer = call_llm(prompt)

        return f"""
# 🧩 Problem Started

## Hint Level: 1/5

{answer}
"""

    # ======================================
    # CAPTURE NEXT MESSAGE AS QUESTION
    # ======================================

    if session_data[
        "awaiting_question"
    ]:

        question = user_input.strip()

        session_data[
            "manual_question"
        ] = question

        session_data[
            "active_question"
        ] = question

        session_data[
            "hint_level"
        ] = 1

        session_data[
            "awaiting_question"
        ] = False

        pattern = detect_pattern(
            question
        )

        session_data[
            "current_pattern"
        ] = pattern

        prompt = get_hint_prompt(
            question,
            1
        )

        answer = call_llm(prompt)

        return f"""
# 🧩 Problem Started

## Hint Level: 1/5

{answer}
"""

    # ======================================
    # NEXT HINT
    # ======================================

    if any(
        x in text
        for x in [
            "hint",
            "next",
            "more"
        ]
    ):

        if not session_data[
            "active_question"
        ]:

            return """
⚠️ No active problem.

Start with:
go raiz

OR upload a file first.
"""

        # ======================================
        # MAX LIMIT
        # ======================================

        if session_data[
            "hint_level"
        ] >= 5:

            return """
✅ Maximum hint level reached.

Now ask:
- show code
- solution
"""

        # ======================================
        # NEXT LEVEL
        # ======================================

        session_data[
            "hint_level"
        ] += 1

        level = session_data[
            "hint_level"
        ]

        question = session_data[
            "active_question"
        ]

        prompt = get_hint_prompt(
            question,
            level
        )

        answer = call_llm(prompt)

        return f"""
# 💡 Hint Level: {level}/5

{answer}
"""

    # ======================================
    # FULL SOLUTION
    # ======================================

    if any(
        x in text
        for x in [
            "show code",
            "solution",
            "full code"
        ]
    ):

        if not session_data[
            "active_question"
        ]:

            return """
⚠️ No active problem.
"""

        question = session_data[
            "active_question"
        ]

        context = retrieve_context(
            question
        )

        prompt = f"""
You are Raiz AI.

QUESTION:
{question}

REFERENCE:
{context}

Provide:

1. Optimal explanation
2. Time complexity
3. Space complexity
4. Full Python solution
"""

        return call_llm(prompt)

    # ======================================
    # SOLVED
    # ======================================

    if "solved" in text:

        session_data[
            "hint_level"
        ] = 0

        # ======================================
        # NEXT QUESTION
        # ======================================

        if session_data[
            "questions"
        ]:

            session_data[
                "current_question"
            ] += 1

            if (
                session_data[
                    "current_question"
                ] >= len(
                    session_data[
                        "questions"
                    ]
                )
            ):

                return """
🎉 All questions solved!
"""

            next_q = session_data[
                "questions"
            ][
                session_data[
                    "current_question"
                ]
            ]

            session_data[
                "active_question"
            ] = next_q

            session_data[
                "hint_level"
            ] = 1

            pattern = detect_pattern(
                next_q
            )

            session_data[
                "current_pattern"
            ] = pattern

            prompt = get_hint_prompt(
                next_q,
                1
            )

            answer = call_llm(prompt)

            return f"""
# ✅ Next Problem

## Hint Level: 1/5

{answer}
"""

        return """
🎉 Problem completed!
"""

    # ======================================
    # NORMAL CHAT
    # ======================================

    memory = get_memory()

    history = "\n".join(
        [
            f"User: {m['user']}\nBot: {m['bot']}"
            for m in memory[-3:]
        ]
    )

    context = retrieve_context(
        user_input
    )

    prompt = f"""
You are Raiz AI DSA Mentor.

Conversation History:
{history}

REFERENCE:
{context}

QUESTION:
{user_input}

Rules:
- concise answer
- mentorship style
- avoid long explanations
"""

    answer = call_llm(prompt)

    save_memory(
        user_input,
        answer
    )

    return answer