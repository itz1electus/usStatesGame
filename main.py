import turtle as t
import pandas as pd


state_text = t.Turtle()
state_text.hideturtle()
state_text.penup()

screen = t.Screen()
image = "blank_states_img.gif"
screen.title("US-states-game")
screen.addshape(image)

t.shape(image)

data = pd.read_csv("50_states.csv")
list_of_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(f"{len(guessed_states)}/50 states guessed",
                                  prompt="Guess the name of the next state: ")
    user_answer = user_guess.title()

    if user_answer == "Exit":
        missing_states = []
        for state in list_of_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if user_answer in list_of_states:
        guessed_states.append(user_answer)
        state_data = data[data.state == user_answer]
        state_text.goto(int(state_data.x), int(state_data.y))
        state_text.write(f"{user_answer}", align='center', font=("Arial", 10, "normal"))
