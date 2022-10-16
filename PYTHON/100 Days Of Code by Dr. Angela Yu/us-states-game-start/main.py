import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")
data = pandas.read_csv("50_states.csv")
x = data[data["x"]]
y = data[data["y"]]
print(x)
# turtle.goto(x=x , y=y)
# if answer_state in data["state"]:
#     turtle.goto(x=data["x"], y=data["y"])
    # turtle.goto()

# print(states)


# turtle.mainloop()