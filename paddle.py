from turtle import Turtle


RESIZE_FACTOR = 3
JUMP_SIZE = 20 * RESIZE_FACTOR


class Paddle(Turtle):
    start_x = 0
    start_y = 0

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=0.1 * RESIZE_FACTOR, stretch_len=RESIZE_FACTOR)
        self.penup()
        self.start_x = x
        self.start_y = y
        self.goto(self.start_x, self.start_y)

    def up(self):
        self.setheading(90)
        self.forward(JUMP_SIZE)

    def down(self):
        self.setheading(270)
        self.forward(JUMP_SIZE)
