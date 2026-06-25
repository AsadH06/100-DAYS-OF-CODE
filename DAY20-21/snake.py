# ─────────────────────────────────────────────────────────────
#  snake.py — Snake class
#
#  Models the snake: a list of Turtle segment objects that move
#  in formation. The head leads; every other segment follows the
#  one in front of it.
#
#  OOP concepts here:
#    Composition  — Snake HAS-A list of Turtle objects (segments)
#    Encapsulation — all snake logic (movement, direction, growth,
#                    reset) lives inside this class. main.py just
#                    calls snake.move(), snake.extend(), snake.reset().
#    Constants    — direction angles and movement distance defined
#                   at module level in ALL_CAPS: clear intent, easy to change.
# ─────────────────────────────────────────────────────────────
from turtle import Turtle

# ── Module-level constants ─────────────────────────────────
# Defined outside the class — these are fixed values that never change.
# ALL_CAPS naming is the Python convention for constants.
# Using named constants instead of raw numbers (e.g. seth(90)) makes
# the direction methods readable and the angles easy to adjust.
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]  # head first, then body segments, spaced 20px apart
MOVE_DISTANCE = 20   # pixels per tick — matches segment size so snake moves cleanly, no gaps
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # segments holds all Turtle objects that make up the snake, head first.
        # Type hint list[Turtle] documents what's inside — not just any list.
        self.segments: list[Turtle] = []

        self.create_snake()               # populates self.segments with 3 starting turtles
        self.head = self.segments[0]      # convenience reference — avoids writing self.segments[0] everywhere
                                          # head is not a separate object; it's an alias pointing to segments[0]

    def create_snake(self):
        # Loops through STARTING_POS and creates one segment per coordinate.
        # Delegates actual turtle creation to add_segment() — single responsibility at method level.
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        # Creates a single white square turtle and places it at the given position.
        # All segment setup lives here — extend() and create_snake() both call this,
        # so there's no duplicated turtle-creation logic.
        t = Turtle(shape="square")
        t.penup()           # prevents lines being drawn as segments move each tick
        t.color('white')
        t.goto(pos)         # places this segment at the given (x, y) coordinate
        self.segments.append(t)

    def extend(self):
        # Grows the snake by one segment.
        # New segment spawns at the tail's current position (segments[-1]).
        # segments[-1] — Python negative indexing: -1 is always the last element.
        # .pos() returns the turtle's current (x, y) as a tuple, which add_segment() accepts.
        #
        # For the first tick the new segment overlaps with the tail.
        # On the next move() call, the tail steps forward but the new segment
        # stays one step behind — naturally becoming the new tail.
        self.add_segment(self.segments[-1].pos())

    def move(self):
        # Moves the snake forward by one tick.
        #
        # Core algorithm: each segment steps into the position of the one ahead of it.
        # The head then moves forward independently.
        #
        # Why reverse order (tail → second segment, not head → tail)?
        # If we went front to back:
        #   seg[1] copies head's position → seg[1] has moved
        #   seg[2] copies seg[1]'s position → but seg[1] already moved! seg[2] goes to the wrong place.
        #
        # Going tail to front means every segment reads its neighbour's
        # ORIGINAL position before that neighbour has moved. Order is critical.
        #
        # range(len-1, 0, -1) → counts down from the last index to index 1 (not 0).
        # Index 0 (head) is excluded here — it moves separately with forward() below.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()   # x of the segment ahead
            new_y = self.segments[seg_num - 1].ycor()   # y of the segment ahead
            self.segments[seg_num].goto(new_x, new_y)   # step into that position

        # Move the head forward LAST — after all other segments have updated.
        # forward() moves in the direction the head is currently facing (set by seth()).
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        # Restarts the snake after a collision.
        # Can't just delete turtles — they'd still be visible on screen.
        # goto(1000, 1000) moves each segment off-screen (outside the 600px window) to hide it.
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()   # empties the list so create_snake() starts fresh
        self.create_snake()
        self.head = self.segments[0]   # re-establish the head reference after the new list is built

    # ── Direction methods ──────────────────────────────────
    # Each method guards against a 180° reversal.
    # If the snake is moving right and the player presses left,
    # the head would instantly reverse into the body — instant death.
    # The != check prevents turning into the directly opposite direction.
    # Only 90° turns (perpendicular directions) are allowed.
    #
    # seth() sets an absolute heading — not relative to current direction.
    # The constants UP/DOWN/LEFT/RIGHT are the degree values turtle uses.

    def up(self):
        if self.head.heading() != DOWN:     # can't go up if currently going down
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:       # can't go down if currently going up
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:    # can't go left if currently going right
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:     # can't go right if currently going left
            self.head.seth(RIGHT)