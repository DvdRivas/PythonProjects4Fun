from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank=[]
for q in question_data:
    question_bank.append(Question(q["text"],q["answer"]))
    
quizz=QuizzBrain(question_bank)
while quizz.still():
    quizz.ask()
    print(f"Your current score is: {quizz.score}/{quizz.number_of_question}")
    print("\n")
print(f"You've completed the quest! \n Your final score was: {quizz.score}/{quizz.number_of_question}")