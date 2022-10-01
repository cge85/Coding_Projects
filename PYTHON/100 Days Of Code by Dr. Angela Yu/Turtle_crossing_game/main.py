from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Crossing")


player = Player()
scoreboard = Scoreboard()



screen.onkey(player.move_up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    player.finish_line()
    scoreboard.update_score()
    screen.update()

screen.exitonclick()




