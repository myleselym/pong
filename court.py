from turtle import Turtle
import time
COURT_CORDS = [(-390, -390), (390, -390), (390, 390), (-390, 390)]
ALIGNMENT = "center"
FONT = ("Courier", 50, 'bold')


class Court(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-390, 390)
        self.pendown()
        self.speed(8.5)
        for cords in COURT_CORDS:
            self.goto(cords)
        self.penup()
        self.goto(0, 390)
        while self.ycor() > -385:
            self.pendown()
            self.goto(0, (self.ycor() - 20))
            self.penup()
            self.goto(0, (self.ycor() - 20))

    def count_down(self, countdown, count):
        self.goto(0, -40)
        self.write(countdown[count], align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.undo()
