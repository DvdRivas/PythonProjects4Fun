from turtle import Turtle
from Score_Board import ScoreBoard
from random import choice
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
colores = ["red", "blue", "yellow", "green", "orange", "pink", "purple", "white", "black", "gray"]
class Snake:
    def __init__(self):
        self.snake=[]
        self.reset()

    def create(self):
        piece = Turtle(shape="turtle")
        piece.penup()
        piece.color(choice(colores))
        self.snake.append(piece)

    def reset(self):
        self.snake.clear()
        piece = Turtle(shape="turtle")
        piece.penup()
        piece.color("white")
        self.snake.append(piece)
        self.create()
        self.create()

    def start_again(self):
            for pieces in self.snake:
                pieces.goto(1000,1000)
            self.reset()
    def move(self):
        for pieces in range(len(self.snake) - 1, 0, -1):
            self.snake[pieces].goto(self.snake[pieces - 1].xcor(), self.snake[pieces - 1].ycor())
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)


    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)