import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

score = 0
correct_guesses = []
all_states = data.state.to_list()
while len(correct_guesses) < 50:
    answer_state = screen.textinput(
        f"{score}/50 States Correct", "What's another state name?"
    ).title()

    if answer_state == "Exit":
        missing_states = [
            [state for state in all_states if state not in correct_guesses]
        ]

        df_missing_states = pandas.DataFrame(missing_states)
        df_missing_states.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        tim = Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state, align="center", font=("Arial", 8, "normal"))
        correct_guesses.append(answer_state)
        score += 1
