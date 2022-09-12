from turtle import Screen, Turtle, onscreenclick
import random

tim = Turtle()
tim.shape("turtle")
tim.color("DeepSkyBlue2", "SpringGreen")

colors = ["blue", "coral","cyan","beige"]

def draw_shape(shape):
    shapes = 360/shape
    for _ in range(shape):
        tim.forward(100)
        tim.right(shapes)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
    


screen = Screen()
screen.exitonclick()

