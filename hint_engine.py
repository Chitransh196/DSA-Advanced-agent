from retriever import retrieve_context


def get_hint_prompt(question, level):

    context = retrieve_context(question)

    # LEVEL 1
    if level == 1:

        return f"""
You are a DSA mentor.

REFERENCE:
{context}

QUESTION:
{question}

Give ONLY:
- best pattern
- intuition

No solution.
"""

    # LEVEL 2
    elif level == 2:

        return f"""
REFERENCE:
{context}

QUESTION:
{question}

Give a small directional hint.
"""

    # LEVEL 3
    elif level == 3:

        return f"""
REFERENCE:
{context}

QUESTION:
{question}

Give medium-level hint.
Mention useful data structure.
"""

    # LEVEL 4
    elif level == 4:

        return f"""
REFERENCE:
{context}

QUESTION:
{question}

Give strong approach hint.
"""

    # LEVEL 5
    elif level == 5:

        return f"""
REFERENCE:
{context}

QUESTION:
{question}

Give pseudocode only.
NO full code.
"""