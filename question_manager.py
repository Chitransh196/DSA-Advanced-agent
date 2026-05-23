from difficulty_classifier import classify_difficulty


def sort_questions_by_difficulty(questions):

    easy = []
    medium = []
    hard = []

    for q in questions:

        diff = classify_difficulty(q)

        if "easy" in diff:
            easy.append(q)

        elif "medium" in diff:
            medium.append(q)

        else:
            hard.append(q)

    return easy + medium + hard