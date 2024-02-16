from turtle import Turtle
POS = [(-250,250), (250,250)]
class Scores(Turtle):

    def __init__(self):
        super().__init__()
        self.users = []
        self.score_user_1 = 0
        self.score_user_2 = 0
        self.create_users()


    def create_users(self):
        for i in range(0,2):
            score = Turtle()
            score.hideturtle()
            score.penup()
            score.color("white")
            score.goto(POS[i])
            self.users.append(score)


    def update_score(self):
        self.users[0].clear()
        self.users[1].clear()
        self.users[0].write(arg=f"{self.score_user_1}", align="center", font=("Trebuchet MS", 24, 'bold'))
        self.users[1].write(arg=f"{self.score_user_2}", align="center", font=("Trebuchet MS", 24, 'bold'))