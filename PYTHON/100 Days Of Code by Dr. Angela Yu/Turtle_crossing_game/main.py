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
car_manager = CarManager()


screen.listen()
screen.onkeypress(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.moving_cars()
    
    #Detect succesful crossing
    if player.ycor() > 280:
        scoreboard.point()
        player.finish_line()
        car_manager.move_increment()
    
    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    




screen.exitonclick()




