# from retriever1 import retrieve_context


# def get_hint_prompt(question, level):

#     context = retrieve_context(question)

#     # LEVEL 1
#     if level == 1:

#         return f"""
# You are a DSA mentor.

# REFERENCE:
# {context}

# QUESTION:
# {question}

# Give ONLY:
# - best pattern
# - intuition

# No solution.
# """

#     # LEVEL 2
#     elif level == 2:

#         return f"""
# REFERENCE:
# {context}

# QUESTION:
# {question}

# Give a small directional hint.
# """

#     # LEVEL 3
#     elif level == 3:

#         return f"""
# REFERENCE:
# {context}

# QUESTION:
# {question}

# Give medium-level hint.
# Mention useful data structure.
# """

#     # LEVEL 4
#     elif level == 4:

#         return f"""
# REFERENCE:
# {context}

# QUESTION:
# {question}

# Give strong approach hint.
# """

#     # LEVEL 5
#     elif level == 5:

#         return f"""
# REFERENCE:
# {context}

# QUESTION:
# {question}

# Give pseudocode only.
# NO full code.
# """



from retriever1 import retrieve_context


def get_hint_prompt(
    question,
    level
):

    context = retrieve_context(question)

    # LEVEL 1
    if level == 1:

        return f"""
You are Raiz AI.

Your job:
ONLY guide.
DO NOT solve.

QUESTION:
{question}

REFERENCE:
{context}

STRICT RULES:
- Return ONLY the pattern name
- Return ONLY one-line intuition
- Maximum 2 lines
- NO algorithm
- NO explanation
- NO code
- NO steps
- NO pseudocode
"""

    # LEVEL 2
    elif level == 2:

        return f"""
You are Raiz AI.

QUESTION:
{question}

STRICT RULES:
- Give ONLY one small directional hint
- Maximum 2 lines
- NO solution
- NO code
- NO pseudocode
"""

    # LEVEL 3
    elif level == 3:

        return f"""
You are Raiz AI.

QUESTION:
{question}

STRICT RULES:
- Give medium-level hint
- Mention useful data structure
- NO complete logic
- NO code
"""

    # LEVEL 4
    elif level == 4:

        return f"""
You are Raiz AI.

QUESTION:
{question}

STRICT RULES:
- Give strong logical hint
- Mention key observation
- Still NO full solution
- NO code
"""

    # LEVEL 5
    elif level == 5:

        return f"""
You are Raiz AI.

QUESTION:
{question}

STRICT RULES:
- Give ONLY pseudocode
- NO real code
- NO complexity analysis
"""