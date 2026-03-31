# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    def next_question(self):
        current_q = self.q_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}: {current_q.text} (True/False)?: ").lower()
        self.check_answer(user_ans, current_q.answer)

    def check_answer(self, user_a, correct_a):
        if user_a == correct_a.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_a}. \nYour current score is: {self.score}/{self.question_number}")



