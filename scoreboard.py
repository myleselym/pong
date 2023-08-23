from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 370)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Player 1: {self.l_score}            Player 2: {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)