import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4  # NOTE: was 10 originally, way too aggressive — game became unplayable fast

class CarManager:

    def __init__(self):
        self.cars: list[Turtle] = []       # stores all active car turtle objects
        self.speed = STARTING_MOVE_DISTANCE  # instance variable so it can be modified per level
        # NOTE: originally MOVE_INCREMENT was a module constant, had to move speed to instance
        # variable so main.py could modify it via car.increase_speed()

    # randomly decides whether to spawn a car this tick
    # 1 in 6 chance per tick naturally spaces cars out — no need for timers or counters
    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.penup()                              # don't draw lines while moving
            car.color(random.choice(COLORS))
            car.goto(290, random.randint(-250, 250)) # spawn at right edge, random y within screen
            car.seth(180)                            # face left
            car.shapesize(stretch_len=2)             # stretch to 40px wide, 20px tall
            self.cars.append(car)

    # moves every active car left by current speed value
    def move_car(self):
        for car in self.cars:
            car.forward(self.speed)  # forward works because car is facing 180 (left)

    # called every level up — increases speed for all future move_car() calls
    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    # removes cars that have gone off the left edge of screen
    # NOTE: must iterate over self.cars[:] (a slice copy), NOT self.cars directly
    # modifying a list mid-iteration skips elements — classic Python pitfall
    # hideturtle() makes car invisible on screen before removing from list
    # DO NOT use car.reset() — it's a built-in Turtle method that moves turtle back to
    # center screen visibly, which is the opposite of what we want
    def remove_car(self):
        for car in self.cars[:]:
            if car.xcor() < -300:
                car.hideturtle()       # hide visually before removing from list
                self.cars.remove(car)  # remove from list to free memory