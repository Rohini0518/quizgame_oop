from data import question_data
from question_model import Question
from quizbrain import QuizBrain

question_bank=[]
for que in question_data:
    # print(que["question"],que["correct_answer"])
    question_bank.append(Question(que["question"],que["correct_answer"]))
# print(question_bank[1].question)   
# print(question_bank[1].correct_answer)
print(len(question_bank)) 
# for ram in question_bank:
#     print(ram.question)
rho=len(question_bank)
quiz=QuizBrain(question_bank)

while quiz.still_there_questions():
    quiz.next_question()
       
