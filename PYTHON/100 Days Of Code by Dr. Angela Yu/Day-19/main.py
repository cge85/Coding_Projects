from turtle import Turtle, Screen

cliff = Turtle()
screen = Screen()

def move_forward():
    cliff.forward(25)

def move_backward():
    cliff.backward(25)

def move_counter_clockwise():
    cliff.right(-10)
    cliff.forward(10)

def move_clockwise():
    cliff.right(10)
    cliff.forward(10)

def clear():
    cliff.penup()
    cliff.clear()
    cliff.home()
    cliff.pendown()
    


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()