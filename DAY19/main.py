# ─────────────────────────────────────────────────────────────
#  Day 19 — Etch-A-Sketch (Keyboard-Controlled Turtle)
#
#  The turtle is controlled with arrow keys in real time.
#  Pressing 'c' clears the drawing and resets the turtle home.
#
#  New concept: Event-driven programming
#  Instead of a sequential top-to-bottom script, this program
#  sets up *listeners* and *callbacks*, then hands control to the
#  screen's event loop. Nothing happens until a key is pressed —
#  the program just waits and responds.
#
#    s.listen()           → tells the Screen to start watching for keyboard events
#    s.onkey(fun, key)    → registers a callback: "when this key is pressed, call this function"
#    s.exitonclick()      → starts the event loop (keeps the window alive and listening)
# ─────────────────────────────────────────────────────────────
from turtle import Turtle, Screen

t = Turtle()
s = Screen()
# t.hideturtle()    # commented out — left visible here so you can see the turtle's direction
s.colormode(255)    # RGB integer mode — not used in this file but set for potential color use


# ── Callback functions ─────────────────────────────────────
# Each function below is a "callback" — a function you define but don't call yourself.
# You pass it to s.onkey() and the Screen calls it for you whenever the key is pressed.
#
# Important: the functions are passed WITHOUT parentheses → fun=move_forward
# Parentheses would CALL the function immediately at setup time.
# Without parentheses, we're passing the function itself as a reference —
# so the Screen can call it later when the key event fires.

def move_forward():
    # Moves the turtle 10px in whatever direction it's currently facing.
    # forward() always moves relative to the turtle's current heading.
    t.forward(10)

def move_backward():
    # Moves the turtle 10px in the opposite of its current heading.
    t.backward(10)

def turn_left():
    # Rotates the turtle 10° counter-clockwise.
    # seth() sets an absolute heading — we add 10 to the current heading
    # to get a relative left turn.
    # t.heading() returns the current direction in degrees (0° = right, 90° = up).
    # seth(heading + 10) → turn left by 10°
    t.seth(t.heading() + 10)

def turn_right():
    # Rotates the turtle 10° clockwise.
    # Subtracting 10 from the heading turns right (clockwise in turtle's coordinate system).
    t.seth(t.heading() - 10)

def clear_screen():
    # Resets the drawing without closing the window.
    # Four steps in order:
    #   1. t.clear()   — erases all drawn lines; turtle stays in current position
    #   2. t.penup()   — lifts pen so the home() move doesn't draw a line back to centre
    #   3. t.home()    — teleports turtle back to (0,0) and resets heading to 0° (facing right)
    #   4. t.pendown() — puts pen back down so the next move draws again
    t.clear()
    t.penup()
    t.home()
    t.pendown()


# ── Setting up the event listeners ────────────────────────
# s.listen() — activates keyboard listening on the Screen.
# Without this call, s.onkey() registers the bindings but nothing fires.
# Think of it as "turning on" the keyboard input.
s.listen()

# s.onkey(fun, key) — binds a key to a callback function.
# When the registered key is pressed, the Screen calls the given function.
# Note: no parentheses after the function name — we pass the function object, not its return value.
s.onkey(fun=move_forward, key="Right")
s.onkey(fun=move_backward, key="Left")
s.onkey(fun=turn_left, key="Up")
s.onkey(fun=turn_right, key="Down")
s.onkey(fun=clear_screen, key='c')   # 'c' for clear — not a directional key, a reset shortcut


# ── Starting the event loop ────────────────────────────────
# s.exitonclick() keeps the window open and the event loop running.
# The program now just waits — it does nothing until a key is pressed,
# then fires the matching callback, then goes back to waiting.
# Clicking the window closes it and ends the program.
s.exitonclick()