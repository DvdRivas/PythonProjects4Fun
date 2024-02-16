from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.score_level_up()



    def score_level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center",font=FONT)

    def game_over(self):
        self.home()
        self.write(arg=f"GAME OVER", align="center", font=FONT)