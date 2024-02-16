import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
score = Scoreboard()
player = Player()
car_manager = CarManager()
screen.onkey(player.move_forward,"Up")
game_is_on = True
while game_is_on:
    car_manager.MoveCars()
    if player.ycor() >= 280:
        score.score_level_up()
        player.StartingPosition()
        car_manager.SetSpeed(score.level)
    time.sleep(0.1)
    screen.update()
    for car in car_manager.cars:
        if player.distance(car) <= 10:
            score.game_over()
            game_is_on = False
screen.exitonclick()