# ─────────────────────────────────────────────────────────────
#  quiz_brain.py — QuizBrain class
#
#  The "brain" of the quiz — owns all the quiz state and logic:
#    - which question we're currently on (question_number)
#    - the list of questions (q_list)
#    - the current score (score)
#    - how to ask a question and check the answer
#
#  OOP concept — Single Responsibility:
#  QuizBrain's job is to run the quiz. It doesn't know where the
#  questions came from (that's data.py's concern) or what a question
#  looks like internally (that's Question's concern). It just receives
#  a list of Question objects and operates on them.
#
#  OOP concept — State management:
#  question_number and score are instance attributes that change
#  throughout the object's lifetime. The object "remembers" where
#  it is in the quiz across multiple method calls — this is the
#  core value of objects over plain functions.
# ─────────────────────────────────────────────────────────────
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0    # index of the current question; starts at 0
        self.q_list = q_list        # the full list of Question objects
        self.score = 0              # incremented each time the user answers correctly

    def still_has_questions(self):
        # Returns a boolean — True if there are still questions left, False otherwise.
        # Used directly as the while loop condition in main.py:
        #   while quiz.still_has_questions(): ...
        #
        # This is a clean OOP pattern: instead of exposing the internal numbers
        # and letting main.py do the comparison itself, we wrap the logic in a
        # method with a readable name. main.py doesn't need to know *how* we
        # track progress — just whether it should keep going.
        return self.question_number < len(self.q_list)

    def next_question(self):
        # Fetch the current Question object using question_number as the index.
        # self.q_list[0] is the first question, self.q_list[1] the second, etc.
        current_q = self.q_list[self.question_number]

        # Increment BEFORE displaying the question number to the user.
        # This means when we're on index 0, the user sees "Q1:" — more natural.
        # It also means self.question_number always reflects how many questions
        # have been *asked* so far, which is what the score display uses.
        self.question_number += 1

        # input() displays the question text and waits for user input.
        # .lower() normalises the input so "True", "TRUE", "true" all match.
        user_ans = input(f"Q{self.question_number}: {current_q.text} (True/False)?: ").lower()

        # Delegate answer checking to its own method — keeps next_question()
        # focused on asking, not on judging. Single responsibility at method level.
        self.check_answer(user_ans, current_q.answer)

    def check_answer(self, user_a, correct_a):
        # correct_a comes in as "True" or "False" (capitalised strings from data.py).
        # .lower() on correct_a normalises it to match the lowercased user input.
        # This means the comparison is always lowercase vs lowercase — no case mismatch.
        if user_a == correct_a.lower():
            self.score += 1         # modifies instance state — score persists on the object
            print("You got it right!")
        else:
            print("That's wrong.")

        # Prints after every question regardless of correct/incorrect.
        # self.score and self.question_number are both read directly from instance state —
        # no need to pass them in; the method already has access via self.
        print(f"The correct answer was: {correct_a}. \nYour current score is: {self.score}/{self.question_number}")