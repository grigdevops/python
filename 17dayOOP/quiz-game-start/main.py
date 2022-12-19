from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
# Testing Purpose
# question = Question(question_data[0]["text"], question_data[0]["answer"])
# question_bank.append(question)


for i in range(0,len(question_data)):
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed teh quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


