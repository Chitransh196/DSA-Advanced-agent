import re


def extract_questions(text):

    raw_questions = re.split(
        r'\n\d+[\.\)]',
        text
    )

    questions = []

    for q in raw_questions:

        q = q.strip()

        if len(q) > 30:
            questions.append(q)

    return questions