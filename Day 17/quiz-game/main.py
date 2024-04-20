from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for dict in question_data:
    question = str(dict["question"])
    answer = str(dict["correct_answer"])
    new_q = Question(question, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
