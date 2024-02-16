#10X10 circulos en toda la ventana 
#Espacio entre circulos de 50 
#20 de radio del circulo
from turtle import Turtle,Screen
from random import choice as ch 
rgb=[(17, 137, 72), (6, 34, 55), (7, 51, 31), (21, 187, 118), (9, 101, 53), (152, 172, 11), (211, 236, 223), (48, 10, 26), (119, 108, 28), (35, 26, 12), (95, 202, 155), (27, 109, 137), (177, 9, 69), (124, 225, 181), (83, 91, 13), (156, 56, 104), (6, 86, 108)]


tortuga = Turtle()
tortuga.shape("turtle")
tortuga.pensize(20)
my_screen = Screen()
my_screen.exitonclick()
tortuga.forward(100)

#tortuga.setx(20)

#for i in range(10):
    