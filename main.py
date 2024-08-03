from data import question_data
from question_model import Question
from quizbrain import QuizBrain

question_bank=[]
for que in question_data:
    # print(que["question"],que["correct_answer"])
    question_bank.append(Question(que["question"],que["correct_answer"]))

quiz=QuizBrain(question_bank)

while quiz.still_there_questions():
    quiz.next_question()
print("Heyy, you completed the quiz game")
print(f"your final score is {quiz.score}/{len(question_bank)}")       
