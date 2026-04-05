from turtle import Turtle
import random

STARTING_POSITION = (0, -280)  # bottom center of 600px screen
MOVE_DISTANCE = 10             # pixels per keypress
FINISH_LINE_Y = 280            # top boundary, triggers level up
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()  # don't draw lines while moving
        self.seth(90)  # face upward (north)
        self.new_level()  # set initial position and heading on creation

    # resets player to starting position for new level
    # NOTE: penup() called here instead of __init__ because goto() is also called here
    # keeping related setup together is cleaner
    def new_level(self):
        self.color(random.choice(COLORS))  # random color each level for visual feedback
        self.goto(STARTING_POSITION)

    # moves turtle forward (upward since heading is 90)
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # returns True if turtle has crossed the finish line, False otherwise
    # NOTE: used ternary expression (return True if ... else False)
    # simpler alternative: return self.ycor() > FINISH_LINE_Y (same result, more concise)
    def check_cross(self):
        return True if self.ycor() > FINISH_LINE_Y else False