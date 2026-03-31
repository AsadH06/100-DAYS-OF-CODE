from typing import List

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


qn_obj: List[Question] = []

for item in question_data:
    qn_obj.append(Question(item['text'], item['answer']))

quiz = QuizBrain(qn_obj)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

