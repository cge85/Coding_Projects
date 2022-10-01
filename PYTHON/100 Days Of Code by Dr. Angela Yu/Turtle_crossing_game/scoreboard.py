from turtle import Turtle


FONT = ("Courier", 24, "normal")
SCORE = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {SCORE}", align="left", font=(FONT))
        self.hideturtle()
        self.update_score()


    def update_score(self):
        ...