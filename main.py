from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

FONT = ("Courier", 40, "bold")

screen = Screen()

screen.tracer(False)

screen.title("Pong")
screen.setup(height=800, width=900)
screen.bgcolor("black")

scoreboard = Scoreboard()

COUNTDOWN = [3, 2, 1]
count = Turtle()
count.color("white")
count.hideturtle()
count.penup()
count.goto(0, -30)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.tracer(True)

for c in range(3):
    count.write(f"{COUNTDOWN[c]}", align="center", font=FONT)
    time.sleep(1)
    count.undo()

ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


def pong():
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor() > 380 or ball.ycor() < -380:
            ball.bounce_y()
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(
                left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        if ball.xcor() > 420:
            scoreboard.increase_l_score()
            scoreboard.update_scoreboard()
            for i in range(3):
                count.write(f"{COUNTDOWN[i]}", align="center", font=FONT)
                time.sleep(1)
                count.undo()
            ball.r_paddle_miss()
        if ball.xcor() < -420:
            scoreboard.increase_r_score()
            scoreboard.update_scoreboard()
            for i in range(3):
                count.write(f"{COUNTDOWN[i]}", align="center", font=FONT)
                time.sleep(1)
                count.undo()
            ball.l_paddle_miss()


pong()

screen.exitonclick()
