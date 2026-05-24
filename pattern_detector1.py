# from llm_client import call_llm
# from retriever1 import retrieve_context


# def detect_pattern(question):

#     context = retrieve_context(question)

#     prompt = f"""
# You are an expert DSA mentor.

# Use the reference knowledge below
# to identify the BEST pattern.

# REFERENCE:
# {context}

# QUESTION:
# {question}

# Return ONLY:
# - pattern name
# - one-line intuition
# """

#     return call_llm(prompt)



from llm_client import call_llm
from retriever1 import retrieve_context


def detect_pattern(question):

    context = retrieve_context(question)

    prompt = f"""
You are a DSA pattern classifier.

QUESTION:
{question}

REFERENCE:
{context}

Choose ONLY ONE BEST pattern.

Examples:
- Hash Map
- Sliding Window
- Two Pointers
- Binary Search
- DP
- BFS
- DFS
- Greedy

Return format:
Pattern: <name>
Intuition: <one line>

DO NOT solve.
"""

    return call_llm(prompt)