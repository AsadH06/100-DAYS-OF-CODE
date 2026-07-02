# ─────────────────────────────────────────────────────────────
#  Day 28 — Pomodoro Timer (Tkinter GUI)
#
#  Implements the Pomodoro Technique:
#    - 25 min work → 5 min short break → repeat
#    - Every 4th work session → 20 min long break
#    - A checkmark appears after each completed work session
#
#  New library: tkinter
#  tkinter is Python's standard GUI (Graphical User Interface) library.
#  It's built into Python — no install needed.
#  Instead of printing to a terminal, tkinter creates real desktop windows
#  with buttons, labels, canvases, and images that users can interact with.
#
#  Core tkinter pattern:
#    1. Create a root window (Tk())
#    2. Add widgets (Label, Button, Canvas, etc.)
#    3. Position widgets with a layout manager (.grid(), .pack(), .place())
#    4. Start the event loop (window.mainloop())
#  mainloop() hands control to tkinter — it listens for events (clicks,
#  key presses, timer callbacks) and responds until the window is closed.
#
#  `from tkinter import *` imports everything from tkinter into the global
#  namespace — so you write `Label(...)` instead of `tkinter.Label(...)`.
#  This is common for tkinter specifically; generally avoid `import *`
#  elsewhere as it can cause name collisions.
# ─────────────────────────────────────────────────────────────
from tkinter import *


# ─────────────────────────────────────────────────────────────
#  CONSTANTS
#
#  ALL_CAPS naming convention signals these are fixed values.
#  Centralising them here means changing WORK_MIN = 25 to 30
#  updates the entire program — no hunting through functions.
# ─────────────────────────────────────────────────────────────
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# Colors stored as hex strings — the standard web color format:
# "#RRGGBB" where each pair is a hex value 00–FF (0–255 in decimal).
# e.g. "#e7305b" → R=231, G=48, B=91 → a vivid red.

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✔"     # Unicode character — Python 3 strings are Unicode by default


# ── Mutable global state ───────────────────────────────────
# These variables track state across multiple function calls.
# `global` keyword is needed inside functions to reassign them
# (modifying a dict/list doesn't need global, but reassigning a
# plain variable like reps = 0 does — same rule as the coffee machine).
reps = 0        # counts how many sessions have started (work + break combined)
counter = 0     # counts completed work sessions → drives the checkmark display
timer = None    # holds the ID returned by window.after() — needed to cancel the timer


# ─────────────────────────────────────────────────────────────
#  reset_timer()
#
#  Cancels any running countdown and restores everything to
#  the initial state: label text, checkmarks, rep count, display.
#
#  New concept — window.after_cancel(id)
#  window.after() (used in count_down) schedules a function call
#  in the future and returns a unique integer ID for that scheduled call.
#  after_cancel(id) cancels that scheduled call using its ID.
#  Without this, the old timer would keep running invisibly after reset.
# ─────────────────────────────────────────────────────────────
def reset_timer():
    global counter, reps
    window.after_cancel(timer)                  # cancels the scheduled count_down call
    label_timer.config(text="Timer", fg=GREEN)  # .config() updates a widget's properties after creation
    label_checkmark.config(text="")             # clears the checkmark row
    reps, counter = 0, 0                        # multiple assignment on one line — resets both counters
    canvas.itemconfig(timer_text, text="00:00") # itemconfig() updates a canvas item's properties
                                                # timer_text is the ID returned by canvas.create_text()


# ─────────────────────────────────────────────────────────────
#  start_timer()
#
#  Called when Start is clicked, and also automatically by
#  count_down() when a session ends — so sessions chain together.
#
#  Session sequence (driven by reps):
#    rep 1 → Work
#    rep 2 → Short break  (+1 checkmark)
#    rep 3 → Work
#    rep 4 → Short break  (+1 checkmark)
#    ...
#    rep 8 → Long break
#    rep 9 → Work  (cycle repeats)
#
#  reps % 8 == 0 catches every 8th rep (8, 16, 24...) → long break
#  reps % 2 == 0 catches every even rep (2, 4, 6...) → short break
#  else          catches every odd rep  (1, 3, 5...) → work
#
#  The % (modulo) operator returns the remainder of division.
#  e.g. 8 % 8 = 0, 10 % 2 = 0, 7 % 2 = 1.
#  Order of the if/elif matters: % 8 must come before % 2
#  because 8 is also divisible by 2 — if reversed, rep 8 would
#  incorrectly trigger a short break instead of a long one.
# ─────────────────────────────────────────────────────────────
def start_timer():
    global reps, counter
    reps += 1   # increment first so rep 1 = first session

    work_sec = WORK_MIN * 60               # convert minutes to seconds for count_down()
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # Long break after every 4 work sessions (rep 8, 16, 24...)
        label_timer.config(text="BREAK", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        # Short break after odd-numbered work sessions (rep 2, 4, 6...)
        counter += 1
        # check_mark * counter → string multiplication: "✔" * 3 = "✔✔✔"
        # This is a clean way to build a repeating string without a loop.
        label_checkmark.config(text=check_mark * counter)
        label_timer.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)

    else:
        # Work session — all odd reps (1, 3, 5, 7...)
        label_timer.config(text="WORK", fg=GREEN)
        count_down(work_sec)


# ─────────────────────────────────────────────────────────────
#  count_down(count)
#
#  Counts down from `count` seconds to 0, updating the canvas
#  display once per second. When it hits 0, starts the next session.
#
#  New concept — window.after(ms, function, *args)
#  Schedules `function` to be called after `ms` milliseconds.
#  This is tkinter's way of doing timed loops — you CAN'T use
#  time.sleep() in a tkinter program because sleep() freezes the
#  entire GUI (the window becomes unresponsive).
#  after() is non-blocking: it registers the call and immediately
#  returns control to the event loop, keeping the UI live.
#
#  window.after(50, count_down, count-1) means:
#  "In 50ms, call count_down(count-1)."
#  count_down then calls after() again → creating a recursive loop
#  that runs until count reaches 0. This is called a recursive timer.
#  NOTE: 50ms per tick is much faster than 1 second (1000ms).
#  This means the timer runs at 20x speed — each "second" on the
#  display actually passes in 50ms. Likely left this way for testing.
#  Change to after(1000, ...) for a real 1-second-per-tick timer.
#
#  Formatting:
#  count // 60 → floor division: strips seconds, gives whole minutes
#  count % 60  → remainder: gives leftover seconds after removing minutes
#  f"0{count_sec}" if count_sec < 10 → zero-pads single digits (9 → "09")
#  This is an inline if-else (ternary expression): value_if_true if condition else value_if_false
# ─────────────────────────────────────────────────────────────
def count_down(count):
    global timer
    count_min = count // 60   # floor division → whole minutes only (e.g. 90 // 60 = 1)
    count_sec = count % 60    # remainder → leftover seconds     (e.g. 90 % 60 = 30)

    # Zero-pad single-digit seconds and minutes for display: 5 → "05"
    # Ternary (inline if-else): expression = value_a if condition else value_b
    count_sec = f"0{count_sec}" if count_sec < 10 else count_sec
    count_min = f"0{count_min}" if count_min < 10 else count_min

    # itemconfig() updates the canvas text item's "text" property.
    # timer_text is the integer ID returned by canvas.create_text() — used to reference that specific item.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Schedule the next tick — decrement count by 1 and call again in 50ms.
        # The return value is an integer ID saved to `timer` so reset_timer() can cancel it.
        timer = window.after(50, count_down, count - 1)
    else:
        # count hit 0 — session complete. Start the next session automatically.
        # count_down calls start_timer calls count_down → sessions chain indefinitely.
        start_timer()


# ─────────────────────────────────────────────────────────────
#  UI SETUP
#
#  New concept — tkinter widgets
#  Every visible element in a tkinter window is a "widget".
#  Common widgets used here:
#    Tk()     → the root window itself (there can only be one)
#    Canvas   → a drawing area — can hold images, shapes, and text items
#    Label    → displays text (not interactive)
#    Button   → clickable element; `command=` binds a callback function
#
#  New concept — .grid() layout manager
#  tkinter has three layout managers: pack, place, and grid.
#  grid() positions widgets in an invisible table of rows and columns.
#  row=0 col=1 → top centre, row=1 col=1 → middle centre, etc.
#  You don't define the grid dimensions — tkinter infers them from the widgets you place.
#
#  Layout used here:
#    col 0    col 1      col 2
#    row 0             "Timer" label
#    row 1             Canvas (tomato + timer text)
#    row 2  [Start]               [Reset]
#    row 3             checkmarks
# ─────────────────────────────────────────────────────────────

# Tk() creates the root window — the desktop window everything lives inside.
# There should only ever be one Tk() instance in a program.
window = Tk()
window.title("pomodoro")
# .config() sets properties on the window itself:
# pady/padx → internal padding in pixels (space between window edge and contents)
# bg        → background color
window.config(pady=50, padx=100, bg=YELLOW)


# ── Canvas widget ──────────────────────────────────────────
# Canvas is a blank drawing area. Unlike Label (which just shows text),
# Canvas can hold images, shapes, lines, and text — all as independent "items".
# Each item gets an integer ID when created, used later to update it with itemconfig().
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# highlightthickness=0 removes the default blue focus border around the canvas.

# PhotoImage loads an image file. Only supports .png and .gif natively.
# Must be assigned to a variable — if it's only referenced inside create_image(),
# Python's garbage collector deletes it and the image disappears (a common tkinter gotcha).
tomato_img = PhotoImage(file="tomato.png")

# create_image(x, y, image=) places the image on the canvas.
# (100, 112) is the centre of the 200×224 canvas.
canvas.create_image(100, 112, image=tomato_img)

# create_text(x, y, ...) places a text item on the canvas.
# Returns an integer ID stored in timer_text — used later in itemconfig() to update the display.
# fill= sets text color (canvas uses "fill" not "fg").
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)   # place the canvas in the grid


# ── Label widgets ──────────────────────────────────────────
# Label displays static or updateable text.
# font= takes a tuple: (font_name, size, style) — same pattern as turtle's write().
# fg= sets foreground (text) color. bg= must match window background to blend in.
label_timer = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0, column=1)


# ── Button widgets ─────────────────────────────────────────
# Button creates a clickable element.
# command= takes a function reference (no parentheses) — called when clicked.
# This is the same callback pattern from Day 19's keyboard bindings.
button_start = Button(text="Start", command=start_timer, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
button_start.grid(row=2, column=0)   # left column

button_reset = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
button_reset.grid(row=2, column=2)   # right column

# Checkmark label starts empty — text is set dynamically in start_timer()
label_checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
label_checkmark.grid(row=3, column=1)


# ── Event loop ─────────────────────────────────────────────
# window.mainloop() starts tkinter's event loop — this is the equivalent
# of screen.exitonclick() in turtle, but more powerful.
# It keeps the window open and continuously listens for:
#   - user events (button clicks, key presses)
#   - scheduled callbacks (window.after() calls)
# The program stays here until the window is closed.
# Nothing written after mainloop() will ever run (while the window is open).
window.mainloop()