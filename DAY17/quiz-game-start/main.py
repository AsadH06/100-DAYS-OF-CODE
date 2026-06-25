# ─────────────────────────────────────────────────────────────
#  main.py — Entry point of the Quiz App
#
#  This file does three things:
#    1. Builds a list of Question objects from raw data
#    2. Feeds that list into a QuizBrain object
#    3. Runs the quiz loop until all questions are exhausted
#
#  Notice the pattern: raw data (question_data) gets converted
#  into objects (Question instances) before anything else happens.
#  The rest of the program never touches the raw data again —
#  it only works with objects. This is a common OOP data pipeline.
# ─────────────────────────────────────────────────────────────
from typing import List

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# ── Building the question bank ─────────────────────────────
# qn_obj will hold a list of Question objects.
# Type hint List[Question] makes it explicit what this list contains —
# not strings, not dicts, but fully-formed Question instances.
# This is optional in Python but good practice: it documents intent
# and helps IDEs flag mistakes early.
qn_obj: List[Question] = []

# question_data is a list of dicts: [{"text": "...", "answer": "..."}, ...]
# We loop through each dict and create a Question object from it,
# then append that object to qn_obj.
# After this loop, qn_obj is a list of structured objects instead of
# a list of raw dicts — the data has been "upgraded" into typed objects.
for item in question_data:
    qn_obj.append(Question(item['text'], item['answer']))

# Debug / sanity check line — prints the object at index 1.
# Without a __repr__ or __str__ method on Question, this prints something like
# <question_model.Question object at 0x...> — useful to confirm objects exist.
print(qn_obj[1])


# ── Setting up the quiz ────────────────────────────────────
# QuizBrain receives the full list of Question objects.
# From here, QuizBrain owns the quiz state: which question we're on,
# the score, and the logic for asking and checking answers.
quiz = QuizBrain(qn_obj)


# ── Running the quiz loop ──────────────────────────────────
# still_has_questions() returns a boolean — True if there are
# questions remaining, False when we've reached the end.
# The while loop keeps calling next_question() until it returns False.
# All the input/output during the quiz happens inside QuizBrain methods —
# this loop itself has no logic, just delegation.
while quiz.still_has_questions():
    quiz.next_question()

# Post-quiz summary — reads score and question_number directly
# off the QuizBrain object as public attributes.
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")