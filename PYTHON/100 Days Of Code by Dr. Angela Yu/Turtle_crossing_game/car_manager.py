from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_cars = random.randint(1, 6)
        if random_cars == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_movement = random.randint(-220, 220)
            new_car.goto(300,y_movement)
            self.all_cars.append(new_car)
        
    def moving_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def move_increment(self):
        self.car_speed += MOVE_INCREMENT
