from turtle import *
import random

tim=Turtle()
direction = [0,90,180,270]
color = ["medium turquoise","chocolate","slate blue","forest green","teal","gold","light green","midnight blue"]

tim.pensize(10)
tim.speed("fastest")

for i in range(200):
    tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(direction))



scr = Screen()
scr.exitonclick()