import turtle as t
import random

tim=t.Turtle()
t.colormode(255)
direction = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_color = (r,b,g)
    return random_color
tim.pensize(1)
tim.speed("fastest")

for i in range(20000):
    tim.color(random_color())
    tim.forward(5)
    tim.setheading(random.choice(direction))
scr = t.Screen()
scr.exitonclick()