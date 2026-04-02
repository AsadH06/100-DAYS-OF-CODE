import random
from turtle import Turtle, Screen


is_race_on = False
colors = ["red","orange","yellow","green","blue","purple"]
screen = Screen()
screen.colormode()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtle_list: list[Turtle] = []
x = -220
y = -160

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x = x, y = y)
    turtle_list.append(new_turtle)
    y += 60

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The blue turtle is the winner!")

        speed = random.randint(0, 10)
        turtle.fd(speed)








screen.exitonclick()