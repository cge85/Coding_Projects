from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color = random.choice(COLORS)
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=3)

    