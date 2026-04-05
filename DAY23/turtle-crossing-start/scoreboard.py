from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"

# Scoreboard inherits from Turtle, uses write() to display level on screen
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()         # hide turtle arrow, only want the text
        self.penup()              # don't draw lines when moving
        self.color("black")       # black text on white background
        self.goto(-280, 260)      # top left corner of screen
        self.level = 0            # starts at 0 because display_score() increments before writing
        self.display_score()      # write initial "LEVEL 1" on creation

    # clears previous level text, increments level, rewrites
    # NOTE: same pattern as snake scoreboard — start at 0, increment first, then write
    # avoids text stacking on screen (clear() before every write)
    def display_score(self):
        self.clear()
        self.level += 1
        self.write(arg=f"LEVEL {self.level}", align=ALIGNMENT, font=FONT)

    # called on collision — moves to center and writes game over
    # no clear() so level text remains visible alongside game over message
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)