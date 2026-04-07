from turtle import Turtle

FONT = ('Courier', 8, 'normal')

class Mapping(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("Black")
        self.penup()

    def write_on_map(self, x, y, state_name):
        self.goto(x, y)
        self.write(arg=f"{state_name}", align="center", font=FONT)

    def guessed(self):
        self.goto(0,0)
        self.write(arg="ALREADY GUESSED\nTry Again...", align="center", font=('Courier', 24, 'normal'))

