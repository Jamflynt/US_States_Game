import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in correct_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        correct_answers.append(answer_state)

        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()

        state_row = data[data.state == answer_state]
        x = int(state_row["x"])
        y = int(state_row["y"])
        state_name.goto(x, y)
        state_name.write(answer_state)




turtle.mainloop()