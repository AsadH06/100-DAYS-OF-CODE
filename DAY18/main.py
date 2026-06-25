# ─────────────────────────────────────────────────────────────
#  Day 18 — Turtle Graphics
#
#  Two new objects introduced here:
#
#  Turtle — a cursor that moves around a canvas and draws as it moves.
#           Think of it as a pen attached to a robot: you give it
#           directions (forward, turn, lift pen) and it draws accordingly.
#
#  Screen — the window/canvas that the Turtle draws on.
#           Controls the display settings: color mode, window behavior, etc.
#
#  Both come from Python's built-in `turtle` module — no install needed.
#  The coordinate system: (0, 0) is the centre of the screen.
#  Positive x → right, positive y → up. Turtle starts facing right (0°).
# ─────────────────────────────────────────────────────────────
import random
from turtle import Turtle, Screen

# ── Setting up the Turtle and Screen objects ───────────────
timmy = Turtle()
timmy.shape('turtle')   # sets the cursor icon to a turtle shape
                        # other options: 'arrow', 'circle', 'square', 'triangle', 'classic'
timmy.hideturtle()      # hides the turtle icon while drawing — cleaner visual output
                        # use timmy.showturtle() to make it visible again

screen = Screen()

# colormode(255) tells the Screen to accept RGB values in the 0–255 range.
# The default colormode is 1.0 (floats: 0.0 to 1.0).
# Switching to 255 lets us pass in standard RGB tuples like (120, 45, 200).
screen.colormode(255)

# speed(0) is the fastest setting — disables animation delay entirely.
# Range is 1 (slowest) to 10 (fast), with 0 meaning "no animation, just draw".
timmy.speed(0)


# ── Commented-out scratch work ─────────────────────────────
# These lines were exploratory — drawing a square, moving, checking position.
# Leaving them commented is a normal part of learning and iterating.

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# timmy.left(90)
# timmy.forward(100)
# print(timmy.pos())   # pos() returns current (x, y) coordinates as a tuple
# timmy.home()         # moves turtle back to (0,0) and resets heading to 0°
# timmy.clear()        # clears all drawings but leaves turtle in place
# print(timmy.pos())


# ─────────────────────────────────────────────────────────────
#  dashed_line()
#
#  Draws a horizontal dashed line by alternating pen down and pen up.
#
#  pendown() → pen touches canvas; moving forward draws a line
#  penup()   → pen lifts off canvas; moving forward leaves no trace
#
#  Pattern per iteration: draw 10px → skip 10px → repeat 10 times
# ─────────────────────────────────────────────────────────────
def dashed_line():
    for i in range(10):
        timmy.pendown()
        timmy.forward(10)   # draws a 10px segment
        timmy.penup()
        timmy.forward(10)   # moves 10px without drawing — creates the gap


# ─────────────────────────────────────────────────────────────
#  random_color()
#
#  Generates a random RGB color as a tuple: (r, g, b)
#  Each channel (red, green, blue) is an integer from 0 to 255.
#
#  Returns a tuple, not a string — works because screen.colormode(255)
#  was set above. Without that, timmy.color() would reject integers.
#
#  random.randint(a, b) returns a random integer N such that a <= N <= b.
#  Both endpoints are inclusive — unlike range(), which excludes the end.
# ─────────────────────────────────────────────────────────────
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b   # Python packs three values into a tuple automatically


# ─────────────────────────────────────────────────────────────
#  draw_shape()
#
#  Draws every regular polygon from triangle (3 sides) to decagon (10 sides),
#  each in a random color, all centered at the same origin.
#
#  Key geometry:
#    To close any regular polygon, the turtle must turn a total of 360°.
#    Dividing 360 by the number of sides gives the exterior angle per turn.
#    e.g. triangle → 360/3 = 120°, square → 360/4 = 90°, hexagon → 60°
#
#  timmy.color() accepts an (r, g, b) tuple here because colormode is 255.
#  range(3, 11) → 3, 4, 5, 6, 7, 8, 9, 10 (11 is excluded)
# ─────────────────────────────────────────────────────────────
def draw_shape():
    for sides in range(3, 11):
        angle = 360 / sides          # exterior angle for this polygon
        timmy.color(random_color())
        for shape in range(sides):   # draw one side per iteration
            timmy.forward(50)
            timmy.right(angle)       # turn by the exterior angle after each side


# ─────────────────────────────────────────────────────────────
#  random_walk()
#
#  Moves the turtle 200 steps in random cardinal directions,
#  changing color every step — produces a colorful, unpredictable path.
#
#  directions: only 0°, 90°, 180°, 270° — keeps movement axis-aligned.
#
#  timmy.seth(angle) — "set heading" — points the turtle in an absolute
#  direction regardless of where it was facing before.
#  Different from timmy.right()/left() which turn *relative* to current heading.
#    seth(0)   → face right
#    seth(90)  → face up
#    seth(180) → face left
#    seth(270) → face down
#
#  timmy.heading() — returns the turtle's current heading in degrees.
#  Stored in `head` here but not actually used — likely a leftover
#  from an earlier experiment.
#
#  pensize(5) → sets line thickness to 5 pixels (default is 1).
# ─────────────────────────────────────────────────────────────
def random_walk():
    directions = [0, 90, 180, 270]
    timmy.pensize(5)
    timmy.speed(0)
    for steps in range(200):
        timmy.color(random_color())
        timmy.forward(10)
        head = timmy.heading()                  # reads current heading (unused — leftover)
        timmy.seth(random.choice(directions))   # picks a random direction from the list


# random_walk()   # commented out — draw_spirograph() is the active function below


# ─────────────────────────────────────────────────────────────
#  spirograph() — student's version
#
#  Draws a spirograph by repeatedly drawing full circles and rotating
#  the turtle's heading slightly before each one.
#
#  timmy.circle(100) → draws a complete circle with radius 100px.
#  The turtle draws the circle moving *forward*, so the direction it
#  faces determines where the circle goes.
#
#  timmy.seth(i) → sets heading to i degrees before each circle.
#  range(1, 364, 4) → steps of 4°: 1, 5, 9, 13 ... up to 361.
#  This draws roughly 90 circles (364/4), each rotated 4° from the last.
#
#  Note: range starts at 1, not 0, and steps by 4 — a manual approach.
#  The teacher's version below calculates this automatically from a gap size.
# ─────────────────────────────────────────────────────────────

"""MY VERSION"""
def spirograph():
    for i in range(1, 364, 4):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.seth(i)   # set absolute heading to i before drawing the next circle


# ─────────────────────────────────────────────────────────────
#  draw_spirograph(size_of_gap) — teacher's version
#
#  Cleaner approach: takes a gap angle as a parameter and calculates
#  everything else automatically.
#
#  int(360 / size_of_gap) → figures out exactly how many circles are
#  needed to complete a full 360° rotation with no gaps or overlap.
#  e.g. gap of 10° → 360/10 = 36 circles; gap of 5° → 72 circles.
#
#  Key difference from the student version:
#    Student: seth(i) — sets heading to an absolute value that grows each loop.
#    Teacher: seth(timmy.heading() + size_of_gap) — adds the gap to the
#             *current* heading each time. Relative rotation, not absolute.
#             More robust: works correctly regardless of starting direction.
#
#  _ as loop variable → convention for "I don't need this value".
#  We only care about how many times we loop, not the iteration number itself.
# ─────────────────────────────────────────────────────────────

"""Ma'am version"""
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):   # _ means the loop count isn't needed
        timmy.color(random_color())
        timmy.circle(100)
        timmy.seth(timmy.heading() + size_of_gap)   # rotate relative to current heading


draw_spirograph(10)   # draws 36 circles, each rotated 10° — produces a full spirograph


# ─────────────────────────────────────────────────────────────
#  screen.exitonclick()
#
#  Keeps the turtle window open and waiting.
#  Without this, the window closes immediately after drawing finishes.
#  Clicking anywhere on the window closes it cleanly.
#  Always the last line in a turtle program.
# ─────────────────────────────────────────────────────────────
screen.exitonclick()