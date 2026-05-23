from llm_client import call_llm
from retriever import retrieve_context


def detect_pattern(question):

    context = retrieve_context(question)

    prompt = f"""
You are an expert DSA mentor.

Use the reference knowledge below
to identify the BEST pattern.

REFERENCE:
{context}

QUESTION:
{question}

Return ONLY:
- pattern name
- one-line intuition
"""

    return call_llm(prompt)