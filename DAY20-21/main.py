# ─────────────────────────────────────────────────────────────
#  main.py — Snake Game Entry Point
#
#  Coordinates three objects: Snake, Food, Scoreboard.
#  Runs the game loop, detects collisions, and delegates all
#  responses to the appropriate object's methods.
#
#  New concept: screen.tracer(0) + screen.update()
#  By default, turtle re-renders the screen after every single
#  drawing command. With 3+ objects moving every tick, that's
#  dozens of redraws per frame — visually messy and slow.
#  tracer(0) turns off auto-rendering. screen.update() then
#  renders exactly one complete frame per tick — smooth animation.
#
#  New concept: time.sleep()
#  The game loop runs as fast as Python can execute it — thousands
#  of ticks per second. sleep(0.1) inserts a 100ms pause each tick,
#  giving the snake a consistent, playable speed.
# ─────────────────────────────────────────────────────────────
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# ── Screen setup ───────────────────────────────────────────
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# tracer(0) — disables turtle's automatic screen refresh after every drawing command.
# Without this, you'd see every segment move individually — flickering chaos.
# We now control rendering manually with screen.update() once per tick.
screen.tracer(0)


# ── Object creation ────────────────────────────────────────
# Three independent objects; each manages its own state.
# Snake holds the segments and handles movement.
# Food places itself at a random position immediately on creation.
# Scoreboard reads the high score from file and renders the score display.
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# ── Keyboard bindings ──────────────────────────────────────
# Same event-driven pattern from Day 19 (Etch-A-Sketch).
# screen.listen() activates keyboard input.
# onkey() registers each arrow key to the corresponding Snake direction method.
# The snake methods include 180° reversal guards — pressing Down while moving Up does nothing.
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


# ── Game loop ──────────────────────────────────────────────
# Runs indefinitely (while True / game_is_on) until a collision ends the game.
# Each iteration = one game tick.
# Tick order matters:
#   1. screen.update() — render the current frame first so the player sees the state
#   2. time.sleep()    — pause 100ms to control game speed
#   3. snake.move()    — advance the snake one step
#   4–6. collision checks — respond to what the move produced
game_is_on = True
while game_is_on:

    # Renders one complete frame — all objects are drawn at their current positions.
    # Also processes any queued keyboard events (direction changes).
    screen.update()

    # Controls game speed — 0.1 seconds = 10 ticks per second.
    # Increase to slow the game down; decrease to speed it up.
    time.sleep(0.1)

    snake.move()   # advances the snake: body follows head, head moves forward

    # ── Food collision ─────────────────────────────────────
    # snake.head is a Turtle object. distance() is an inherited Turtle method:
    # it returns the pixel distance between two turtle objects.
    # 15px threshold — slightly larger than the food dot (10px) to feel forgiving.
    # On collision: food relocates, score increments, snake grows by one segment.
    if snake.head.distance(food) < 15:
        food.refresh()              # teleports food to a new random position
        scoreboard.increase_score() # increments score and updates display
        snake.extend()              # adds a segment at the tail


    # ── Wall collision ─────────────────────────────────────
    # xcor() and ycor() — Turtle methods that return current x and y coordinates.
    # The screen is 600px wide/tall, centered at (0,0) → edges at ±300.
    # 280 is used (not 300) to trigger slightly before the visual edge,
    # accounting for the snake segment's own width.
    #
    # game_is_on = False + scoreboard.game_over() is the original "end the game" version.
    # The active version calls reset() on both objects to restart instead of ending.
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        # game_is_on = False        # original: end the game
        # scoreboard.game_over()    # original: show "GAME OVER" text
        scoreboard.reset()          # saves high score if beaten, resets current score to 0
        snake.reset()               # hides all segments off-screen, rebuilds a fresh 3-segment snake


    # ── Self collision ─────────────────────────────────────
    # Loops through all segments EXCEPT the head (segments[1:]).
    # segments[1:] — list slicing: returns everything from index 1 onwards, skipping index 0 (head).
    # If we included the head, distance(head) from head = 0, which is always < 10 — instant false positive.
    #
    # 10px threshold — tighter than food collision; segment size is 20px so 10px means centres are overlapping.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False    # original: end the game
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()