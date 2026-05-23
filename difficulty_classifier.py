from llm_client import call_llm


def classify_difficulty(question):

    prompt = f"""
Classify this DSA problem.

Return ONLY one:
easy
medium
hard

Question:
{question}
"""

    return call_llm(prompt).strip().lower()