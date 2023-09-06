from turtle import Screen, Turtle
from Food import Food
from ScoreBoard import ScoreBoard
import time

from Snake import Snake

# SCREEN SETUP
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create snake
snake = Snake()

# Generate food
food = Food()

# Create scoreboard
scoreBoard = ScoreBoard()

# Control the snake
screen.listen()  # Event listener
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ######################################

    # Detect collison with food
    if snake.head.distance(food.position()) < 16:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()

    ######################################

    # Detect collision with the wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() < -280
        or snake.head.ycor() > 280
    ):
        game_is_on = False
        scoreBoard.game_over()

    ######################################

    # Detect collison on tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreBoard.game_over()

# PREVENT THE SCREEN DISAPEAR
screen.exitonclick()
