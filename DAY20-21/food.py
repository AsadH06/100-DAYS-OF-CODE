# ─────────────────────────────────────────────────────────────
#  food.py — Food class
#
#  New OOP concept: Inheritance
#  Food inherits from Turtle — it IS a Turtle object with all of
#  Turtle's built-in methods (goto, shape, color, distance, etc.)
#  We don't rewrite any of that; we just extend it with our own
#  __init__ setup and a refresh() method.
#
#  Inheritance syntax: class Food(Turtle)
#  This means: "Food is a specialised kind of Turtle."
#  Relationship: IS-A (Food IS A Turtle)
#  Compare to Day 17's coffee machine: Menu HAS-A list of MenuItems (composition).
#  Here: Food IS-A Turtle (inheritance). Different relationship, different syntax.
# ─────────────────────────────────────────────────────────────
import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        # super().__init__() calls the parent class (Turtle) constructor first.
        # This is mandatory when inheriting — without it, the Turtle internals
        # never get set up and none of its methods will work.
        # super() always refers to the parent class.
        super().__init__()

        self.shape('circle')
        self.penup()                # lifts pen — moving to a random position won't draw a line

        # shapesize controls the turtle's visual size.
        # Default turtle shape is 20×20px. stretch values are multipliers:
        # 0.5 × 20 = 10px — makes the food dot small and proportionate to the snake segments.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        self.color("blue")
        self.speed(0)               # instant teleport — no animation delay when refresh() moves it

        # refresh() is called here so food appears immediately when the object is created.
        # No separate setup call needed in main.py — the object is ready the moment it's instantiated.
        self.refresh()

    def refresh(self):
        # Teleports the food to a new random position within the screen boundaries.
        # Screen is 600×600px, centered at (0,0) → edges are at ±300.
        # randint range is ±270 to keep food away from the walls (snake dies near ±280).
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)   # goto() is inherited from Turtle — no need to redefine it