# ─────────────────────────────────────────────────────────────
#  Day 19 — Hirst Painting (Dot Grid)
#
#  Recreates Damien Hirst's spot paintings using Turtle:
#  a 10×10 grid of colored dots, each picked randomly from a
#  palette extracted from a real image using the colorgram library.
#
#  Two parts to this file:
#    1. The colorgram color extraction (commented out — already done)
#    2. The turtle dot-grid drawing (active code)
# ─────────────────────────────────────────────────────────────
import colorgram

# ── colorgram color extraction (commented out) ─────────────
# colorgram is a third-party library that extracts dominant colors
# from an image file and returns them as Color objects with .rgb attributes.
#
# colorgram.extract('image.jpg', n) → returns the n most dominant colors in the image.
# Each color object has a .rgb attribute with .r, .g, .b sub-attributes (0–255 integers).
#
# The loop below reads each color's RGB channels and packs them into a tuple (r, g, b),
# then appends to colors_rgb — building the color_list you see hardcoded below.
# This was run once to generate that list, then commented out since we have the data.
#
# number_of_color = int(input("Enter number of color: "))
# colors = colorgram.extract('image.jpg', number_of_color)
#
# colors_rgb = []
# for color in range(number_of_color):
#     r = colors[color].rgb.r
#     g = colors[color].rgb.g
#     b = colors[color].rgb.b
#     rgb_color = (r, g, b)
#     colors_rgb.append(rgb_color)
# print(colors_rgb)
# ── end of extraction block ────────────────────────────────


from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.bgcolor('black')     # sets canvas background to black — makes colors pop

tim.hideturtle()            # hides the turtle cursor; we're drawing dots, not tracking movement
tim.penup()                 # lifts pen so moving to the start position doesn't draw a line

# colormode(255) — lets tim.dot() and tim.color() accept RGB tuples with integer values 0–255.
# Without this, turtle expects float values between 0.0 and 1.0.
screen.colormode(255)


# ── color palette ──────────────────────────────────────────
# This list was produced by running the colorgram extraction above on a Hirst painting.
# Each tuple is an (r, g, b) color extracted from the actual image.
# Hardcoded here so the program doesn't need the image file to run every time.
color_list = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
    (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
    (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
    (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]


# ── Grid setup ─────────────────────────────────────────────
# The grid is 10×10, with dots spaced 50px apart.
# Starting at (-250, -250) centers the grid on the screen.
#
# Why -250?
#   10 dots × 50px spacing = 500px total width and height.
#   Half of 500 = 250. Starting at -250 means the grid spans
#   from -250 to +250 on both axes — perfectly centered at (0,0).
#
# x stays fixed as the left-edge anchor for each new row.
# y increments by 50 after each row to move up one row at a time.
y = -250   # starting y position (bottom of the grid)
x = -250   # starting x position (left edge of every row)

tim.speed(0)   # fastest speed — no animation delay

# ── Drawing the 10×10 dot grid ─────────────────────────────
# Outer loop (i): controls rows — iterates 10 times, one per row.
# Inner loop (j): controls columns — draws 10 dots across each row.
#
# Structure per outer iteration:
#   1. tim.goto(x, y) — jumps to the left edge of the current row.
#      goto(x, y) moves to an absolute screen coordinate.
#      Because penup() is active, this move draws nothing.
#   2. Inner loop draws 10 dots across, moving right 50px after each.
#   3. y += 50 moves the row anchor up by 50px for the next iteration.
for i in range(10):
    tim.goto(x, y)              # jump to start of this row (pen is up — no line drawn)

    for j in range(10):
        # tim.dot(size, color) — draws a filled circle dot at the current position.
        # size=20 → dot diameter in pixels.
        # random.choice(color_list) → picks a random (r,g,b) tuple from the palette.
        # Each dot is independently randomised — no two runs look the same.
        tim.dot(20, random.choice(color_list))

        # Move right by 50px to the next dot position in this row.
        # fd() is shorthand for forward() — moves in the current heading direction (right by default).
        tim.fd(50)

    y += 50   # shift the row anchor up by 50px before the next row begins


# screen.exitonclick() — keeps the window open after drawing finishes.
# Without this, the window closes instantly. Click anywhere to close it.
screen.exitonclick()