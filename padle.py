from turtle import Turtle

up = 90
down = 270

class Padle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.size = 5
        self.shapesize(stretch_wid=1, stretch_len=self.size)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 300 - self.size * 10:
            self.setheading(up)
            self.forward(35)

    def move_down(self):
        if self.ycor() > -300 + self.size * 10:
            self.setheading(down)
            self.forward(35)

    def change_size(self, expand_size):
        self.size = expand_size
        self.shapesize(stretch_wid=1, stretch_len=self.size)
