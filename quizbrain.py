from question_model import Question


class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0
    def still_there_questions(self):
       return self.question_number< len(self.question_list)
               
    def next_question(self):
        current_question=self.question_list[self.question_number]
        crct_answer=current_question.correct_answer
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.question}.(True/False)?: ").lower()
        self.check_answer(user_answer,crct_answer)
        
        
    def check_answer(self,user_answer,crct_answer):
        if user_answer==crct_answer.lower():
            self.score+=1
            print("Well Done!! ,You guessed it right")    
        else:
            print("Wrong answer")    
        print(f"The correct answer is {crct_answer}")
        print(f"your score is {self.score}/{self.question_number}")
        print("\n")


   