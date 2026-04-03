import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turns off auto-rendering, we control when screen updates

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # tells screen to start listening for keyboard input
screen.onkey(fun=snake.up, key="Up")       # binds Up arrow to snake.up
screen.onkey(fun=snake.down, key="Down")   # binds Down arrow to snake.down
screen.onkey(fun=snake.left, key="Left")   # binds Left arrow to snake.left
screen.onkey(fun=snake.right, key="Right") # binds Right arrow to snake.right

game_is_on = True
while game_is_on:
    screen.update()     # renders the frame AND processes queued key events
    time.sleep(0.1)     # controls game speed (100ms per tick)
    snake.move()

    # food collision: if head is within 15px of food, relocate food, update score, grow snake
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # wall collision: if head crosses any boundary, end the game
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # self collision: skip head (segments[1:]), if head is within 10px of any body segment, end the game
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
            # game_is_on = False

screen.exitonclick()