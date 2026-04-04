from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

LP_POSITION = (-350, 0)  # left paddle starting position
RP_POSITION = (350, 0)   # right paddle starting position

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)  # turns off auto-rendering, we control when screen updates

r_paddle = Paddle(RP_POSITION)  # right paddle instance
l_paddle = Paddle(LP_POSITION)  # left paddle instance
ball = Ball()
score = Scoreboard()

screen.listen()  # start listening for keyboard input
screen.onkeypress(fun=r_paddle.up, key="Up")      # right paddle up
screen.onkeypress(fun=r_paddle.down, key="Down")  # right paddle down
screen.onkeypress(fun=l_paddle.up, key="w")       # left paddle up
screen.onkeypress(fun=l_paddle.down, key="s")     # left paddle down

game_is_on = True

while game_is_on:
    screen.update()               # render current frame and process key events
    time.sleep(ball.move_speed)   # controls game speed, decreases as ball speeds up

    ball.move_ball()

    # wall collision: top and bottom boundaries
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # reverse vertical direction

    # paddle collision: ball near either paddle's x position AND within distance of the paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()  # reverse horizontal direction and increase speed

    # miss detection: ball passed right wall, left player scores
    if ball.xcor() > 380:
        ball.reset_pos()   # return ball to center
        score.l_point()    # increment left player score

    # miss detection: ball passed left wall, right player scores
    if ball.xcor() < -380:
        ball.reset_pos()   # return ball to center
        score.r_point()    # increment right player score

    if score.score_a == 10 and score.score_a > score.score_b:
        score

screen.exitonclick()