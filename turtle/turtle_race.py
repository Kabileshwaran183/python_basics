from turtle import *
import random

# tim = Turtle(shape="turtle")
# a = Turtle(shape="turtle")
# b = Turtle(shape="turtle")
# c = Turtle(shape="turtle")
# d = Turtle(shape="turtle")

scr = Screen()
scr.setup(width=500,height=400)

y_positions = [-100,-50,0,50,100]
c=["red","blue","yellow","green","purple"]

all_turtles = []
for i in range(0,5):
    tim = Turtle(shape="turtle")
    tim.color(c[i])
    tim.penup()
    tim.goto(x=-230,y=y_positions[i])
    all_turtles.append(tim)

user_bet=scr.textinput(title="make a bet",prompt="Choose which turtle wins")
if user_bet:
    race_on = True

while race_on:
    for t in all_turtles:
        if t.xcor()>230 :
            race_on = False
            win_color=t.pencolor()
            if win_color == user_bet:
                print("You won")
            else :
                print("You lose")
        speed = random.randint(0,10)
        t.forward(speed)


# tim.color("yellow")
# a.color("orange")
# b.color("green")
# c.color("blue")
# d.color("red")

# tim.penup()
# a.penup()
# b.penup()
# c.penup()
# d.penup()

# tim.goto(-230,-100)
# a.goto(-230,-50)
# b.goto(-230,0)
# c.goto(-230,50)
# d.goto(-230,100)

scr.exitonclick()
