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
        self.question_number+=1
        ques=input(f"Q.{self.question_number}: {current_question.question}.(True/False)?: ")
        if ques==current_question.correct_answer:
            self.score+=+1
            print("Well Done!! ,You guessed it right")    
            print(f"The correct answer is {current_question.correct_answer}")
            print(f"your score is {self.score}/{self.question_number}")
            return True
        else:
            print("Wrong answer")    
            print(f"The correct answer is {current_question.correct_answer}")
            print(f"your score is {self.score}/{self.question_number}")
            return False
        
# new_q=Question("rohini",True)   
# new_q2=Question("ram",False)   
# que_list=[new_q,new_q2]
# ram=QuizBrain( que_list )
# ram.next_question()

   