from turtle import Turtle
from random import randint,choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.total = len(self.cars)
        self.speed = STARTING_MOVE_DISTANCE
        for i in range(30):
            self.CreateCar()


    def SetSpeed(self,level):
        self.speed = level * MOVE_INCREMENT + STARTING_MOVE_DISTANCE

    def CreateCar(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=2,stretch_wid=1)
        car.color(choice(COLORS))
        car.penup()
        car.goto(randint(-300,300),randint(-250,280))
        self.cars.append(car)


    def MoveCars(self):
        for car in self.cars:
            car.backward(self.speed)
            if car.xcor() <= -300:
                car.goto(300,randint(-250,280))
