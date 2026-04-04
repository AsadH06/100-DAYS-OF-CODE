from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20  # pixels per keypress

# Paddle inherits from Turtle — it IS a turtle, appears on screen and moves directly
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()          # initialize parent Turtle class
        self.shape('square')
        self.color("white")
        self.penup()                # don't draw lines while moving
        self.seth(90)               # face upward so forward/backward maps to up/down
        self.shapesize(stretch_len=5)  # stretch vertically to 100px (5 * 20px default)
        self.goto(position)         # place paddle at given position

    def up(self):
        if self.ycor() >= 250:      # boundary check: top limit (300 - 50 for paddle half-height)
            pass
        else:
            self.forward(MOVE_DISTANCE)  # move up

    def down(self):
        if self.ycor() <= -250:     # boundary check: bottom limit
            pass
        else:
            self.backward(MOVE_DISTANCE)  # move down