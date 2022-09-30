from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


while True:
    time.sleep(0.1)
    screen.update()


screen.listen()

screen.exitonclick()