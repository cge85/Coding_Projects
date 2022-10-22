import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                            prompt="What's another state`s name?").title() # type: ignore

    if answer_state == "Exit":
        states_list = [state for state in all_states if state not in guessed_states]
        states_to_learn = pandas.DataFrame(states_list)
        states_to_learn.to_csv("states_to_learn.csv", index=False)
        break

    if  answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_state = data[data.state == answer_state]
        t.goto(int(data_state.x), int(data_state.y)) #type: ignore
        t.write(answer_state)

