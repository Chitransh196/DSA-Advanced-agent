import random

problems = [
    "Two Sum",
    "Reverse Linked List",
    "Valid Parentheses",
    "Merge Intervals",
    "Binary Search",
    "Longest Substring Without Repeating Characters",
    "Number of Islands",
    "Climbing Stairs",
]


def recommend_problem():
    return f"📌 Try this problem: {random.choice(problems)}"