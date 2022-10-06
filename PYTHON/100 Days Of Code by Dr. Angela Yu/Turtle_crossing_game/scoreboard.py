from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-290, 260)
        self.score_update()
        

    def score_update(self):
        self.clear()
        self.write(f"Level:{self.score}", align="left", font=(FONT))
        
    
    def point(self):
        self.score += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.hideturtle()
        self.write("GAME OVER", align="center", font=(FONT))
        