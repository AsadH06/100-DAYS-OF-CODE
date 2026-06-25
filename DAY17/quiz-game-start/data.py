# ─────────────────────────────────────────────────────────────
#  data.py — Raw question data
#
#  This file is just a data store — no classes, no logic.
#  question_data is a list of dicts, where each dict has two keys:
#    "text"   → the question string
#    "answer" → "True" or "False" (as strings, not booleans)
#
#  Why strings and not Python booleans (True/False)?
#  Because we're comparing against user input from input(), which
#  always returns a string. Keeping answers as strings avoids
#  needing to convert types during comparison.
#
#  OOP note — Separation of concerns:
#  Keeping data in its own file means you can swap out the question
#  set entirely (e.g. load from an API or a JSON file) without
#  touching any of the logic in QuizBrain or Question.
# ─────────────────────────────────────────────────────────────
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]