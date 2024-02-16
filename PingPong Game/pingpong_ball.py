from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.pos_x = self.xcor()
        self.pos_y = self.ycor()

    def create(self):
        pass