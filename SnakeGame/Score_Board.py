from turtle import Turtle
with open("max_score.txt") as memory:
    highest_score = memory.read()
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-10,280)
        self.color("white")
        self.high_score = int(highest_score)
        self.score = -1


    def increase(self):
        self.score += 1
        self.refresh()


    def refresh(self):
        self.clear()
        self.write(arg=f"Your score is: {self.score}    High Score: {self.high_score}", align='center',font=("Bold", 12, 'normal'))

    def finish(self):
        self.goto(0,0)
        self.write(arg=f"Game Over", align='center', font=("Bold", 12, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("max_score.txt",mode="w") as new_high_score:
                new_high_score.write(str(self.high_score))
        self.score = 0
        self.refresh()