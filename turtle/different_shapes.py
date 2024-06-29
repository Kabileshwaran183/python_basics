from turtle import *
import random
tim = Turtle()

colors = ["red","blue","green","orange"]

def draw_shape(no_of_sides):
    angle = 360/no_of_sides
    for i in range(no_of_sides):
        angle = 360/no_of_sides
        tim.forward(50)
        tim.speed(100)
        tim.right(angle)
    tim.color(random.choice(colors))

for i in range(3,25):
    draw_shape(i)


screen = Screen()
screen.exitonclick()