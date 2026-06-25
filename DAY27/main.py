# ============================================================
# TKINTER GUI
# ============================================================

from tkinter import *  # imports all tkinter classes directly into namespace

window = Tk()  # creates the main application window
window.title("My first GUI program")
window.minsize(width=500, height=300)  # sets minimum window size in pixels

# Label — widget that displays text on screen
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()  # pack() places the widget in the window, stacks top to bottom by default
my_label['text'] = "New Text"  # can update widget properties using dict-style access

# button_clicked is DEFINED here but NOT CALLED yet
# at this point user_input doesn't exist yet — but that's fine
# Python only executes the body of this function when the button is actually clicked
# by that time, all the code below has already run and user_input exists in memory
# this is called a CLOSURE — the function "closes over" variables in its surrounding scope
def button_clicked():
    my_label.config(text=user_input.get())  # .config() updates widget properties
                                             # .get() retrieves current text from Entry widget

button = Button(text="click me", command=button_clicked)  # command= binds function to button click
                                                           # NOTE: no () after button_clicked — passing
                                                           # the function itself, not calling it
button.pack()

# Entry — single line text input widget
user_input = Entry(width=30)  # width in characters, not pixels
user_input.pack()
# user_input now exists — so when button_clicked() is eventually called, it can access this

window.mainloop()  # starts the event loop — keeps window open and listens for events
                   # nothing below this line runs until the window is closed