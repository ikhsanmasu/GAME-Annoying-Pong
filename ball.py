from turtle import Turtle
from random import choice, randint

class Ball(Turtle):
    def __init__(self, color="white"):
        super().__init__()
        self.dir_x = choice([-1, 1])
        self.dir_y = choice([-1, 1])
        self.move_x = 2
        self.move_y = 2
        self.penup()
        self.color(color)
        self.shape("circle")

    def move(self):
        new_x = self.xcor() + self.move_x * self.dir_x
        new_y = self.ycor() + self.move_y * self.dir_y
        self.goto(new_x, new_y)
        if self.ycor() > 290 or self.ycor() < -280:
            self.bounce_horizontal()

    def bounce_horizontal(self):
        self.dir_y = - self.dir_y

    def bounce_vertical(self):
        self.dir_x = - self.dir_x

    def increase_speed(self):
        self.move_x += 0.5
        self.move_y += 0.5

    def initial_speed(self):
        self.move_x = 1
        self.move_y = 1

