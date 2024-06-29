import turtle
import pandas

scr = turtle.Screen()
scr.title("U.S states game")
image = "./Desktop/PYTHON COURSE 100days/programs/pandas/us states quiz/us-states-game-start/us-states-game-start/blank_states_img.gif"
scr.addshape(image)
turtle.shape(image)

# def get_mouse_click_pos(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_pos)
# turtle.mainloop()
data = pandas.read_csv("./Desktop/PYTHON COURSE 100days/programs/pandas/us states quiz/us-states-game-start/us-states-game-start/50_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state)<50 :
    answer = scr.textinput(title="Guess the state",prompt=f"{len(guessed_state)} / 50 correct states").title()
    if answer == "Exit" :
    #     missing_states = []
    #     for state in all_states :
    #         if state in guessed_state:
    #             continue
    #         else :
    #             missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_state]
        df = pandas.DataFrame(missing_states)
        print("****************")
        print("STATES TO LEARN")
        print("****************")
        print(df)
        break
    if answer in all_states :
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_state = data[data.state == answer]
        t.goto(int(answer_state.x),int(answer_state.y))
        t.write(answer)

scr.exitonclick()