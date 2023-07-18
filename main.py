import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# Create and move a paddle
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
# Create the ball and make it move
ball = Ball((0, 0))

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")




# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep Score

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
screen.exitonclick()
