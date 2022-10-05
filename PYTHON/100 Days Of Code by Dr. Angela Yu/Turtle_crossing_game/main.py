from turtle import Screen, xcor
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



screen.listen()
screen.onkeypress(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    

    if player.ycor() > 290:
        scoreboard.point()
        player.finish_line()
        




screen.exitonclick()




