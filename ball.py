from turtle import Turtle
import random


# start game function, that throws the ball randomly to some side
# bounce function against wall
# bounce function against paddle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed("fastest")
        self.setheading(random.randint(-360, 360))
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.013

    def bounce_y(self):
        self.y_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def start_over(self):
        self.setheading(random.randint(-360, 360))
        self.goto(0, 0)
