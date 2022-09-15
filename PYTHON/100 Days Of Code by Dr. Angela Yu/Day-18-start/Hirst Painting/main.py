import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

color_list = [(139, 183, 164), (21, 177, 118), (240, 59, 213), (204, 166, 139), (223, 84, 158), (122, 98, 72), (142, 36, 20), (20, 58, 138), (190, 23, 175), (71, 36, 30), (195, 33, 72), (225, 198, 171), (57, 32, 35), (25, 184, 170), (236, 33, 85), (7, 66, 111), (109, 136, 190), (42, 81, 173), (183, 110, 94), (188, 210, 183), (39, 45, 38)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")


steps = 1

while steps <= 10:
    steps += 1
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.left(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)





screen = t.Screen()
screen.exitonclick()