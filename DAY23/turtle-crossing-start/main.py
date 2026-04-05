import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # turns off auto-rendering, we control when screen updates

car = CarManager()
score = Scoreboard()
player = Player()

screen.listen()  # start listening for keyboard input
screen.onkeypress(fun=player.move_up, key="Up")  # only up movement, no other directions

game_is_on = True
while game_is_on:
    time.sleep(0.1)   # controls game speed (fixed, unlike pong where ball controlled sleep)
    screen.update()   # render frame and process key events

    car.create_car()  # randomly spawns a car this tick (1 in 6 chance)
    car.move_car()    # moves all existing cars one step left

    # level up: turtle reached the finish line at top of screen
    if player.check_cross():
        player.new_level()        # reset turtle to bottom, change color
        score.display_score()     # increment and redisplay level
        car.increase_speed()      # cars move faster next level

    # collision detection: check each car against player position
    # NOTE: used abs(x diff) < 20 AND abs(y diff) < 20 instead of distance()
    # because distance() is circular — a car passing close vertically could falsely trigger it
    # abs() check is rectangular, more accurate for car-shaped objects
    for each_car in car.cars:
        if abs(each_car.xcor() - player.xcor()) < 20 and abs(each_car.ycor() - player.ycor()) < 20:
            score.game_over()
            game_is_on = False

    # remove off-screen car s to prevent memory leak
    # NOTE: iterates over self.cars[:] (a copy) — modifying a list while iterating over it
    # directly causes Python to skip elements, classic bug
    car.remove_car()

screen.exitonclick()