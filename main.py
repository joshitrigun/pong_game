import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
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
ball = Ball()
score = Score()
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# Detect when paddle misses
# Keep Score

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()
screen.exitonclick()
