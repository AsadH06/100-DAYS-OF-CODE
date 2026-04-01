import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.hideturtle()
screen = Screen()
screen.colormode(255)
timmy.speed(0)
# timmy.color('red')

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# timmy.left(90)
# timmy.forward(100)
# print(timmy.pos())
# timmy.home()
# timmy.clear()
# print(timmy.pos())

# import heroes
# print(heroes.gen())

def dashed_line():
    for i in range(10):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b
def draw_shape():
    for sides in range(3, 11):
        angle = 360/sides
        timmy.color(random_color())
        for shape in range(sides):
            timmy.forward(50)
            timmy.right(angle)


def random_walk():
    directions = [0, 90, 180, 270]
    timmy.pensize(5)
    timmy.speed(0)
    for steps in range(200):
        timmy.color(random_color())
        timmy.forward(10)
        head = timmy.heading()
        timmy.seth(random.choice(directions))

# random_walk()

"""MY VERSION"""
def spirograph():
    for i in range(1,364, 4):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.seth(i)

"""Ma'am version"""
def draw_spirograph(size_of_gap):
    #calculates how many circles needed automatically
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.seth(timmy.heading()+ size_of_gap)

draw_spirograph(10)







screen.exitonclick()