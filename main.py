import time
from turtle import Screen
from padle import Padle
from ball import Ball
from score import Score
from random import randint, choice
from expand import Expand

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

score = Score()

player1 = Padle((-350, 0))
player2 = Padle((350, 0))

screen.onkeypress(player1.move_up, "w")
screen.onkeypress(player1.move_down, "s")
screen.onkeypress(player2.move_up, "Up")
screen.onkeypress(player2.move_down, "Down")

main_ball = Ball()
balls = [main_ball]
powers = []

game_is_on = True

try:
    while game_is_on:
        chance = randint(1, 500)
        if chance == 50:
            add_ball = Ball(choice(["green"]))
            balls.append(add_ball)

        chance = randint(1, 1000)
        if chance == 50:
            add_ball = Ball(choice(["red"]))
            balls.append(add_ball)

        chance = randint(1, 100)
        if chance == 50:
            expand = Expand()
            powers.append(expand)

        for power in powers:
            power.move()

            if power.distance(player1) < player1.size * 10 and -350 < power.xcor() < -330:
                player1.change_size(choice([40, 1, 40, 5, 20, 40, 1, 40, 1, 5]))
                power.goto(-500,-500)
                powers.remove(power)

            elif power.distance(player2) < player2.size * 10 and 350 > power.xcor() > 330:
                player2.change_size(choice([40, 1, 40, 5, 20, 40, 1, 40, 1, 5]))
                power.goto(-500,-500)
                powers.remove(power)


        for ball in balls:
            ball.move()

            if ball.distance(player1) < player1.size * 10 and -360 < ball.xcor() < -330 or ball.distance(player2) < player2.size * 10 and 360 > ball.xcor() > 330:
                ball.bounce_vertical()
                ball.increase_speed()

            if ball.xcor() > 420:
                score.p1_add_score()
                if ball.color() == ("red", "red"):
                    score.p1_add_score(4)
                ball.initial_speed()
                if ball == main_ball:
                    ball.goto((0, 0))
                else:
                    balls.remove(ball)

            if ball.xcor() < -420:
                score.p2_add_score()
                if ball.color() == ("red", "red"):
                    score.p2_add_score(4)
                ball.initial_speed()
                if ball == main_ball:
                    ball.goto((0, 0))
                else:
                    balls.remove(ball)


        screen.update()
        time.sleep(0.01)

    screen.exitonclick()
except:
    pass


