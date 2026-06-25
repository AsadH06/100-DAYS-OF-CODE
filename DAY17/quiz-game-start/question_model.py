# ─────────────────────────────────────────────────────────────
#  question_model.py — Question class
#
#  This is the simplest class in the project — a pure data model.
#  Its only job is to give structure to a question: bundle its
#  text and answer together into a single named object.
#
#  OOP concept — Modelling real-world things as objects:
#  A question in a quiz naturally has two properties: what it asks
#  and what the correct answer is. A class captures that structure
#  formally. Instead of passing two separate variables (text, answer)
#  around the program, we pass one Question object that carries both.
#
#  OOP concept — Encapsulation (basic form):
#  The text and answer for a question are bound together inside one
#  object. You access them as q.text and q.answer — they can't get
#  separated or mixed up with another question's data.
# ─────────────────────────────────────────────────────────────
class Question:

    # __init__ runs when you do Question("some text", "True").
    # It stores the two arguments as instance attributes on self,
    # making them accessible anywhere via object.text / object.answer.
    def __init__(self, text, answer):
        self.text = text       # the question string shown to the user
        self.answer = answer   # the correct answer string: "True" or "False"