import turtle as t
import random

tim=t.Turtle()
t.colormode(255)
direction = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    color = (r,b,g)
    return color
tim.pensize(1)
tim.speed("fastest")
def draw_spirograph(size_of_gap,radius):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(5,150)
scr = t.Screen()
scr.exitonclick()