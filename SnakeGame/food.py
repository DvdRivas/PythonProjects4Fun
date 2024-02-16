import random
from turtle import Turtle
from Score_Board import ScoreBoard
import random
score = ScoreBoard()
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.create()

    def create(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 290))
        score.increase()

    def game_over(self):
        score.finish()

    def reset(self):
        score.reset()