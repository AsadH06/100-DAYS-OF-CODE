from turtle import Turtle

# Ball inherits from Turtle — appears on screen, uses goto() to move each tick
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()                 # don't draw lines while moving
        self.x_move = 10             # horizontal distance per tick (positive = right)
        self.y_move = 10             # vertical distance per tick (positive = up)
        self.move_speed = 0.1        # sleep duration, decreases on each paddle hit to speed up

    def move_ball(self):
        new_x = self.xcor() + self.x_move  # calculate next x position
        new_y = self.ycor() + self.y_move  # calculate next y position
        self.goto(new_x, new_y)            # move ball to new position

    def bounce_x(self):
        self.x_move *= -1            # reverse horizontal direction
        self.move_speed *= 0.9       # reduce sleep time = ball moves faster each bounce

    def bounce_y(self):
        self.y_move *= -1            # reverse vertical direction

    def reset_pos(self):
        self.goto(0, 0)              # return ball to center
        self.move_speed = 0.1        # reset speed back to default
        self.bounce_x()              # reverse direction so ball goes toward the scorer