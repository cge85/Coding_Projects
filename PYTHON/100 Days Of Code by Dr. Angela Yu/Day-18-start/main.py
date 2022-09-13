# from turtle import Screen, Turtle, onscreenclick, shape
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
# tim.color("DeepSkyBlue2", "SpringGreen")

# Challange 1 Draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# Challange 2 Draw a Dashed Line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Challange 3 Drawing Different Shapes
# colors = ["blue", "coral","cyan","beige"]

# def draw_shapes(shape):
#     shapes = 360 / shape
#     for _ in range(shape):
#         tim.forward(100)
#         tim.right(shapes)

# for shape_number in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shapes(shape_number)


# Challange 4 Generate a Random Walk
# colors = ["BlueViolet", "DeepPink", "LimeGreen", "Cyan", "DeepSkyBlue", "Yellow", "Red"]
def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    colors = (r, b, g)
    return colors


# directions = [0, 90, 180, 270]
# tim.pensize(5)
# tim.speed("fastest")

# for _ in range(200):
#     tim.forward(50)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color()) 

tim.speed("fastest")
# Challange 5 Draw a Spirograph

# Mine
# for _ in range(75):
#     tim.circle(100)
#     tim.left(5)
#     tim.color(random_color())

# Angela`s

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

