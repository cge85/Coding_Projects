from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align="left", font=(FONT))
    
    def point(self):
        self.score += 1
        self.score_update()
