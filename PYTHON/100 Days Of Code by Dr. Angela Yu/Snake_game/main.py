from turtle import Screen, Turtle
import random
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snakes = []

for position in starting_positions:
    snake = Turtle("square")
    snake.color("white")
    snake.penup() 
    snake.goto(position)
    snakes.append(snake)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for snake_number in range(len(snakes) -1, 0, -1):
        new_x = snakes[snake_number - 1].xcor()
        new_y = snakes[snake_number - 1].ycor()
        snakes[snake_number].goto(new_x, new_y)
        
        

screen.exitonclick()