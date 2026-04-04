from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

# Scoreboard inherits from Turtle, uses write() to display scores on screen
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()            # hide the turtle arrow, only want the text
        self.color("white")
        self.penup()                 # don't draw lines when moving
        self.goto(0, 260)            # position near top center of screen
        self.score_a = 0             # left player score
        self.score_b = 0             # right player score
        self.display_score()         # write initial 0 0 on creation

    def display_score(self):
        self.clear()                 # erase previous score text before rewriting
        self.write(arg=f"{self.score_a} \t {self.score_b}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.score_a += 1            # increment left player score
        self.display_score()         # refresh display

    def r_point(self):
        self.score_b += 1            # increment right player score
        self.display_score()         # refresh display

    def game_over(self):
        self.goto(0, 0)              # move to center of screen
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)