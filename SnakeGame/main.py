from turtle import Screen
from Snake_main import Snake
from food import Food
import time
screen = Screen()
i = 0
limit = 280
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)
screen.listen()
food = Food()
snake = Snake()
game_on = True
while game_on:

    snake.move()
    screen.update()
    time.sleep(.1)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    if snake.snake[0].distance(food) < 15:
        food.create()
        snake.create()

    if snake.snake[0].xcor() > limit or snake.snake[0].xcor() < -limit or snake.snake[0].ycor() > limit or snake.snake[0].ycor() < -limit:
        snake.start_again()
        food.reset()

    for parts in snake.snake[1:]:
        if snake.snake[0].distance(parts) < 15:
            snake.start_again()
            food.reset()

food.game_over()
screen.exitonclick()