class QuizzBrain:
    def __init__(self,question_bank):
        self.number_of_question = 0
        self.question_list = question_bank
        self.score = 0

    def ask(self):
        a=self.question_list[self.number_of_question]
        self.number_of_question+=1
        answer=input(f"Q.{self.number_of_question}: {a.question} (True/False): ")
        self.check(answer.capitalize(),a.answer)
        
        
    def still(self):
        return  not self.number_of_question == len(self.question_list)
            
    def check(self, user, correct):
        if user == correct:
            print("You are right!")
            self.score +=1
        else:
            print("Sorry you are wrong")
        print("The correct answer was:", correct)