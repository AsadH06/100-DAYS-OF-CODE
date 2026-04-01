import colorgram

# number_of_color = int(input("Enter number of color: "))
# colors = colorgram.extract('image.jpg', number_of_color)
#
# colors_rgb = []
# for color in range(number_of_color):
#     r = colors[color].rgb.r
#     g = colors[color].rgb.g
#     b = colors[color].rgb.b
#     rgb_color = (r,g,b)
#     colors_rgb.append(rgb_color)
# print(colors_rgb)

from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
screen.bgcolor('black')
tim.hideturtle()
tim.penup()
screen.colormode(255)


color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

y = -250
x = -250
tim.speed(0)
for i in range(10):
    tim.goto(x, y)
    for j in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
    y += 50
# todo: 10x10 matrix of colors
# todo: dot size = 20, spaced by 50 spaces



screen.exitonclick()