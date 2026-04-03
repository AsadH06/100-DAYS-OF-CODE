import random
from turtle import Turtle

# Food inherits from Turtle, so it IS a turtle object with all its drawing capabilities
class Food(Turtle):

    def __init__(self):
        super().__init__()          # initialize the parent Turtle class first
        self.shape('circle')        # set shape to circle to look like food
        self.penup()                # don't draw lines when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # shrink to half size (10x10px instead of default 20x20px)
        self.color("blue")
        self.speed(0)               # instant movement, no animation delay
        self.refresh()              # place food at a random position immediately on creation

    # teleports food to a new random position on the screen
    def refresh(self):
        random_x = random.randint(-270, 270)  # stay within 600px wide screen (boundary at ~280)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)