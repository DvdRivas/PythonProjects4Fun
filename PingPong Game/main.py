from turtle import Screen
from bg_window import Window
import time
screen = Screen()
screen.tracer(0)
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PingPong Game")
screen.listen()
window = Window()
game_on = True
screen.update()
window.Score.update_score()
screen.onkeypress(window.user2_up, "Up")
screen.onkeypress(window.user2_down, "Down")
screen.onkeypress(window.user1_up, "w")
screen.onkeypress(window.user1_down, "s")
while game_on:
    window.ball_forward()
    time.sleep(.01)
    screen.update()
screen.exitonclick()
