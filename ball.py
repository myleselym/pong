from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .0001

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .9

    def reset_ball(self):
        self.bounce_x()
        self.speed("fastest")
        self.goto(x=0, y=0)
        self.speed("slowest")

    def r_paddle_miss(self):
        self.reset_ball()

    def l_paddle_miss(self):
        self.reset_ball()
