from turtle import Turtle

FONT = ("Arial", 12, "bold")
DASH_SIZE = 30


# scoreboard should keep track of left and right scores
# should draw the middle dashed line between the two
# idea 1. import the paddle class here and have a template for a scoreboard that keeps track of
# a paddle to watch
# scoreboard that keeps track of 2 scores and can be updated by passing score name variable + score
# easier ju you don't have to import the paddle class
class Scoreboard(Turtle):
    left = 0
    right = 0

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.draw_divider()
        self.update_score()

    def draw_divider(self):
        self.setheading(90)
        self.goto(0, -300)
        while self.ycor() < 300:
            self.pendown()
            self.forward(DASH_SIZE)
            self.penup()
            self.forward(DASH_SIZE)
        self.penup()

    def update_score(self):
        self.clear()
        self.goto(0, 300)
        self.write("Left : Right", align="center", font=FONT)
        self.goto(0, 280)
        self.write(f"{self.left} : {self.right}", align="center", font=FONT)
