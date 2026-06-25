# ─────────────────────────────────────────────────────────────
#  Day 19 — Turtle Race
#
#  Six turtles race across the screen. The user bets on a color
#  before the race starts. Each turtle moves a random distance
#  per frame. First to cross the finish line wins.
#
#  New concepts:
#    - Creating multiple Turtle objects programmatically (a list of turtles)
#    - screen.textinput() — a GUI popup for user input
#    - screen.setup()     — setting the window size
#    - turtle.xcor()      — reading a turtle's current x coordinate
#    - turtle.pencolor()  — reading the turtle's current color
#    - is_race_on flag    — controlling a while loop with a boolean
# ─────────────────────────────────────────────────────────────
import random
from turtle import Turtle, Screen

# ── Race state flag ────────────────────────────────────────
# Starts as False — the race doesn't begin until the user has placed a bet.
# Set to True only after textinput confirms input was received.
# The while loop below runs only while this is True.
is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.colormode()      # initialises color mode (default 1.0 — uses named colors like "red")
screen.setup(500, 400)  # sets the window size: width=500px, height=400px
                        # without this, the window uses a default size which may not fit the layout

# ── Getting the user's bet via a GUI popup ─────────────────
# screen.textinput() opens a small dialog box with a title and prompt.
# The user types their answer and clicks OK — the return value is that string.
# If the user clicks Cancel or closes the box, it returns None.
# This is the turtle module's built-in alternative to the terminal input() function.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


# ── Building the turtle lineup ─────────────────────────────
# Instead of creating six turtles manually (t1 = Turtle(), t2 = Turtle()...),
# we loop through the colors list and create one turtle per color.
# Each turtle is appended to turtle_list so we can loop through all of them later.
#
# Type hint list[Turtle] — signals this list contains Turtle objects specifically.
turtle_list: list[Turtle] = []

# Starting positions:
# x = -220 → fixed left edge, just inside the left wall (screen is 500px wide, so left edge = -250)
# y = -160 → bottom of the lineup; increments by 60 for each turtle to stack them vertically
# 6 turtles × 60px apart = 360px total height — fits within the 400px window
x = -220
y = -160

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)     # sets both pen color and fill color to the named color
    new_turtle.penup()          # lifts pen so goto() doesn't draw a line to the start position
    new_turtle.goto(x=x, y=y)  # teleports to the starting position using keyword arguments
                                # keyword args (x=x, y=y) used here for clarity — same as goto(-220, y)
    turtle_list.append(new_turtle)
    y += 60                     # shift the next turtle's starting y up by 60px


# ── Starting the race ──────────────────────────────────────
# Only start if the user actually entered something.
# If user_bet is None (cancelled the dialog), is_race_on stays False
# and the while loop never runs.
if user_bet:
    is_race_on = True


# ── Race loop ──────────────────────────────────────────────
# Runs continuously, moving all turtles each iteration, until one crosses the finish line.
#
# Structure per frame:
#   For each turtle:
#     1. Check if it has crossed x = 230 (the finish line — near the right edge)
#     2. If yes — determine the winner, print result, stop the race
#     3. If no  — move it forward by a random amount (0–10px)
#
# random.randint(0, 10) — each turtle gets an independent random step each frame.
# Some turtles may not move at all (0) while others jump ahead (10) — simulates a real race.
while is_race_on:
    for turtle in turtle_list:

        # turtle.xcor() returns the turtle's current x coordinate.
        # 230 is used as the finish line — just before the right edge of the 500px window (250).
        if turtle.xcor() > 230:
            is_race_on = False   # stops the while loop after this iteration

            # turtle.pencolor() reads the turtle's current pen color as a string (e.g. "blue").
            # Used to identify which turtle crossed the finish line.
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                # Bug: hardcodes "blue" instead of using winning_color.
                # Should be: print(f"You've lost! The {winning_color} turtle is the winner!")
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Move this turtle forward by a random distance this frame.
        # Placed outside the if block so ALL turtles keep moving
        # even in the same frame that a winner is detected.
        speed = random.randint(0, 10)
        turtle.fd(speed)


screen.exitonclick()