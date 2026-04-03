from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]  # head first, then body segments
MOVE_DISTANCE = 20  # pixels per tick
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments: list[Turtle] = []
        self.create_snake()         # build the initial 3-segment snake
        self.head = self.segments[0]  # convenience reference to the head segment

    # builds the initial snake by adding a segment at each starting position
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    # creates a single white square turtle at the given position and appends it to segments
    def add_segment(self, pos):
        t = Turtle(shape="square")
        t.penup()           # don't draw lines while moving
        t.color('white')
        t.goto(pos)         # place segment at the given coordinate
        self.segments.append(t)

    # grows the snake by adding a new segment at the current tail position
    # overlaps with tail for one tick, then naturally falls behind as everyone else moves forward
    def extend(self):
        self.add_segment(self.segments[-1].pos())

    # moves the snake forward: each segment steps into the position of the one ahead of it
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):   # tail to second segment (reverse order is critical)
            new_x = self.segments[seg_num - 1].xcor()        # get x of segment ahead
            new_y = self.segments[seg_num - 1].ycor()        # get y of segment ahead
            self.segments[seg_num].goto(new_x, new_y)        # step into that position
        self.head.forward(MOVE_DISTANCE)                      # move head forward last

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # direction methods guard against reversing into yourself (opposite direction check)
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


"""
Key understanding — why reverse order in move()?
If you went front to back instead:
seg[1] → goes to head's position
seg[2] → goes to seg[1]'s NEW position (wrong! seg[1] already moved)
Going tail to front means every segment reads its neighbour's original position before that neighbour moves. Order matters here.
Why the opposite direction guards?
If you're moving right and instantly press left, the head reverses into the body — instant death. The != check prevents that. You can only turn 90 degrees, never 180.
"""