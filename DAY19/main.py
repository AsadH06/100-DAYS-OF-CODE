from turtle import Turtle, Screen

t = Turtle()
s = Screen()
# t.hideturtle()
s.colormode(255)

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.seth(t.heading() + 10)

def turn_right():
    t.seth(t.heading() - 10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(fun=move_forward, key="Right")
s.onkey(fun=move_backward, key="Left")
s.onkey(fun=turn_left, key="Up")
s.onkey(fun=turn_right, key="Down")
s.onkey(fun=clear_screen, key='c')


s.exitonclick()