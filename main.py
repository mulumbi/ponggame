from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(600, 800, "black")
screen.title("2 Player Pong Game")
screen.tracer(0)

# set up paddles, balls and scoreboard
game_on = True
initial_left_x = -398
initial_right_x = 398
initial_y = 290
lefty = Paddle(initial_left_x, initial_y)
righty = Paddle(initial_right_x, initial_y)
pp_ball = Ball()
board = Scoreboard()

# detect keystrokes
screen.listen()
screen.onkey(righty.up, "Up")
screen.onkey(righty.down, "Down")
screen.onkey(lefty.up, "w")
screen.onkey(lefty.down, "s")

# actual running of the game
while game_on:
    screen.update()
    time.sleep(pp_ball.move_speed)
    pp_ball.move()

    # detect collision with right paddle
    if righty.distance(pp_ball) < 30 and pp_ball.xcor() > 360:
        pp_ball.paddle_bounce()

    # detect collision with left paddle
    if lefty.distance(pp_ball) < 30 and pp_ball.xcor() < -360:
        pp_ball.paddle_bounce()

    # detect collision with wall
    if pp_ball.ycor() > 295 or pp_ball.ycor() < -295:
        # proceed to bounce
        pp_ball.bounce_y()

    # score tracker
    if pp_ball.xcor() > 400:
        board.left += 1
        board.update_score()
        pp_ball.start_over()
    elif pp_ball.xcor() < - 400:
        board.right += 1
        board.update_score()
        pp_ball.start_over()
screen.exitonclick()
