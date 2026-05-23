import os
from difflib import SequenceMatcher


# ✅ CHUNKING
def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunks.append(text[i:i + chunk_size])

    return chunks


# ✅ SIMILARITY
def similarity(a, b):

    return SequenceMatcher(
        None,
        a.lower(),
        b.lower()
    ).ratio()


def retrieve_context(query: str) -> str:

    try:

        # ✅ Always correct path
        base_dir = os.path.dirname(
            os.path.abspath(__file__)
        )

        file_path = os.path.join(
            base_dir,
            "dsa_patterns_knowledge_base1.txt"
        )

        if not os.path.exists(file_path):

            return f"❌ File NOT found in: {base_dir}"

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            knowledge = f.read()

        # ✅ CHUNKS
        chunks = chunk_text(knowledge)

        scored_chunks = []

        for chunk in chunks:

            score = similarity(query, chunk)

            scored_chunks.append((score, chunk))

        scored_chunks.sort(reverse=True)

        # ✅ TOP CHUNKS
        top_chunks = scored_chunks[:3]

        context = "\n\n".join(
            [chunk for _, chunk in top_chunks]
        )

        return context

    except Exception as e:

        return f"❌ Error: {e}"