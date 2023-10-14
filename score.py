from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto((0, 260))
        self.write(f"{self.score_p1} : {self.score_p2}", move=False, align="center", font=("Arial", 20, "normal"))

    def p1_add_score(self, num = 1):
        self.score_p1 += num
        self.clear()
        self.write(f"{self.score_p1} : {self.score_p2}", move=False, align="center", font=("Arial", 20, "normal"))

    def p2_add_score(self, num = 1):
        self.score_p2 += num
        self.clear()
        self.write(f"{self.score_p1} : {self.score_p2}", move=False, align="center", font=("Arial", 20, "normal"))

