from turtle import Turtle,Screen
from data import turtles
from random import randint as r
screen = Screen()
screen.setup(width=500, height=400)
tortugas=[]
for i in turtles:
    tortuga = Turtle(shape="turtle")
    tortuga.color(i["name"])
    tortuga.shapesize(2)
    tortuga.penup()
    tortuga.goto(i["pos"])
    tortugas.append(tortuga)
bet = screen.textinput(title="Lets make som bets!",prompt="Which turtle do you think will win")
if bet:
    race = True
while race:
    for i in tortugas:
        if i.xcor() >= 220:
            race = False
            winner = i.pencolor()
            if winner == bet:
                print("Congrats, you win!")
            else:
                print("You loose, good luck the next time")
            print(f"Turtle {i.color()[1]} wins!")
        i.forward(r(1, 10))
screen.exitonclick()


