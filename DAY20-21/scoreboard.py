# ─────────────────────────────────────────────────────────────
#  scoreboard.py — Scoreboard class
#
#  Inherits from Turtle to use its write() method for rendering
#  text directly onto the screen canvas.
#
#  New concept: File I/O for persistent state
#  self.score resets to 0 every game. But self.high_score is read
#  from a file at startup and written back when a new record is set.
#  This is how data survives between program runs — the file acts
#  as simple persistent storage.
# ─────────────────────────────────────────────────────────────
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')   # font tuple: (font_name, size, style)
                                    # style options: 'normal', 'bold', 'italic'


class Scoreboard(Turtle):

    def __init__(self):
        # Calls Turtle's constructor first — required when inheriting.
        # Without this, Turtle's internal state is never initialised.
        super().__init__()

        self.score = 0   # current game score; resets to 0 each time reset() is called

        # ── Reading the high score from a file ────────────
        # open("high_score.txt", mode="r") opens the file in read mode.
        # The `with` block — context manager — ensures the file is automatically
        # closed after the block ends, even if an error occurs.
        # file.read() returns the file contents as a string — int() converts it to a number.
        # Requires high_score.txt to exist with a number inside (e.g. "0").
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.hideturtle()   # hides the turtle arrow — we only want the text, not a cursor
        self.color("white")
        self.penup()        # prevents a line being drawn when the turtle moves to position
        self.goto(0, 265)   # top-centre of the 600px screen (top edge = 300, this is 35px inside)
        self.update_score() # writes the initial "Score: 0 High Score: X" immediately on creation

    def update_score(self):
        # Clears the previous text and rewrites the current values.
        # self.clear() — Turtle method — erases only what THIS turtle has written.
        # Without clear(), each update would stack text on top of the old text.
        # write() places text at the turtle's current position (0, 265).
        #   arg=    → the string to display
        #   align=  → "center" means the text is centered on the turtle's position
        #   font=   → the FONT tuple defined above
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # Moves to screen centre and writes "GAME OVER".
        # Note: NO self.clear() here — intentional.
        # clear() would wipe the score text at the top too.
        # By skipping it, the final score stays visible while "GAME OVER" appears below it.
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        # Called on collision (wall or self) — saves a new high score if beaten, then restarts.

        # ── Updating the high score if beaten ─────────────
        if self.score > self.high_score:
            self.high_score = self.score
            # open(..., mode="w") opens in write mode — overwrites the file entirely.
            # f"{self.high_score}" writes just the number as a string.
            # The `with` block closes the file automatically when done.
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0          # reset current score for the new game
        self.update_score()     # rewrite the display with score=0 and updated high score

    def increase_score(self):
        # Increments score by 1 and immediately refreshes the display.
        # Called from main.py whenever the snake eats food.
        self.score += 1
        self.update_score()