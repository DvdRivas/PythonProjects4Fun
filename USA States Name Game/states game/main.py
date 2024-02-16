import turtle
import pandas
FONT= ("Arial",12,"normal")
def create_turtle(name,x,y):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.color("black")
    state.goto(int(x), int(y))
    state.write(arg=name, align="center", font=FONT)


states = pandas.read_csv("50_states.csv")
total = len(states["state"])
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
corrects = 0
guessed = []
game_on = True
list_of_states = states["state"].to_list()
print(list_of_states)
while len(guessed)  < 50:
    state = screen.textinput(title=f"{corrects}/{total} States Correct",prompt="Write a name of an USA state: ").title()
    if state in list_of_states and state not in guessed:
        corrects+=1
        guessed.append(state)
        cor = states[states.state == state]
        create_turtle(name=state,x=cor.x,y=cor.y)
        print(guessed)
    elif state == "Exit":
        break
missing_estates = list(set(guessed) ^ set(list_of_states))
print(f"{missing_estates}")
print(f"Total of missing states = {len(missing_estates)}")
pandas.DataFrame(missing_estates).to_csv("States_to_study.csv")

screen.exitonclick()

