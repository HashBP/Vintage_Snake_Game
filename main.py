# Tracer() is used for automatic screen update on or off.

from ast import If
from multiprocessing.resource_sharer import stop
from tracemalloc import start
from turtle import Turtle, Screen, color, exitonclick
import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from collison import Collison

screen = Screen()
screen.setup(width=600, height=600)  # Keyword Arguments
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Score Board
score_turtle = Scoreboard()

# Border


def repeat():
    b_turtle.forward(600)
    b_turtle.right(90)


b_turtle = Turtle()
b_turtle.color("white")
b_turtle.hideturtle()
b_turtle.penup()
b_turtle.goto(-300, 300)
b_turtle.pendown()
for i in range(5):
    repeat()

# Create Snake
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move Snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    # Detect collison with food

    if snake.head.distance(food) < 15:
        food.refresh()
        score_turtle.inc_score()
        snake.extend()

    # Detect collison with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        collison = Collison()
        collison.collison_msg()
        game_is_on = False

    # Detect Collison with tail

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            collison = Collison()
            collison.collison_msg()
            game_is_on = False


screen.exitonclick()

