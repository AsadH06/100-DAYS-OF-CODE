from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

# Scoreboard inherits from Turtle, using its write() method to display text on screen
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()          # initialize parent Turtle class
        self.score = 0             # starts at -1 because display_score() increments before writing, so first display shows 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()           # hide the turtle arrow, we only want the text
        self.color("white")
        self.penup()                # don't draw lines when moving
        self.goto(0, 265)           # position at top center of 600px screen
        self.update_score()       # write initial "Score: 0" immediately on creation

    # clears previous score text, increments, and rewrites — avoids text stacking on screen
    def update_score(self):
        self.clear()                # erase whatever was written before at this turtle's position
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # called on game over — moves to center and writes message (no clear, so score stays visible above)
    def game_over(self):
        self.goto(0, 0)             # center of screen
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

"""
Key understanding — why score = -1?
display_score() is called in __init__, and the first thing it does is self.score += 1. So:
-1 + 1 = 0  → displays "Score: 0"  ✓
If it started at 0, the first display would show "Score: 1" which is wrong.
Why no clear() in game_over()?
clear() erases everything this turtle has written. If you called clear() in game_over(), it would wipe the final score text too. By skipping it, both "Score: X" and "GAME OVER" are visible on screen at the same time.
"""