from turtle import Turtle
from scores import Scores
from random import choice, randint
import time
from pingpong_ball import Ball
POS = [(-490,0),(480,0)]
DIR = [(0),(180)]
limit_x = 500
limit_y = 300

#ball = Turtle()
class Window(Turtle):
    
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.pensize(8)
        self.goto(0,-280)
        self.setheading(90)
        while self.ycor() < 320:
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)
        self.create_paddles()
        self.Score = Scores()
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()


    def create_ball(self):
        self.ball.home()
        self.ball.setheading(choice(DIR))

    def ball_forward(self):
        self.ball.forward(5)
        if self.ball.distance(self.paddles[0]) < 30:
            self.ball.setheading(randint(-45,45))
        elif self.ball.distance(self.paddles[1]) < 30:
            self.ball.setheading(randint(135,225))
        else:
            if self.ball.xcor() > limit_x-20:
                self.Score.score_user_1+=1
                self.mark_score()


            elif self.ball.xcor() < -limit_x+10:
                self.Score.score_user_2+=1
                self.mark_score()


        if self.ball.ycor() > limit_y-20 or self.ball.ycor() < -limit_y+20:
            self.ball.setheading(self.ball.heading()+35)

    def mark_score(self):
        self.Score.update_score()
        self.create_ball()
        time.sleep(1)
        self.paddles[0].goto(POS[0])
        self.paddles[1].goto(POS[1])
    def create_paddles(self):
        for i in range(0,2):
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.showturtle()
            paddle.setheading(90)
            paddle.shapesize(stretch_wid=1,stretch_len=3)
            paddle.penup()
            paddle.goto(POS[i])
            self.paddles.append(paddle)


    def user1_up(self):
        if self.paddles[0].ycor() < limit_y-40:
            self.paddles[0].forward(12)

    def user1_down(self):
        if self.paddles[0].ycor() > -limit_y + 40:
            self.paddles[0].backward(12)

    def user2_up(self):
        if self.paddles[1].ycor() < limit_y - 40:
            self.paddles[1].forward(12)

    def user2_down(self):
        if self.paddles[1].ycor() > -limit_y + 40:
            self.paddles[1].backward(12)