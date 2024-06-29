from turtle import *

tim = Turtle()
scr = Screen()

def move():
    tim.forward(10)
def front():
    tim.setheading(90)
    move()
def left():
    tim.setheading(180)
    move()
def right():
    tim.setheading(0)
    move()
def back():
    tim.setheading(270)
    move()

scr.listen()
scr.onkeypress(key = "space",fun=move)
scr.onkeypress(key = "w",fun = front)
scr.onkeypress(key = "a",fun=left)
scr.onkeypress(key = "d",fun = right)
scr.onkeypress(key = "s",fun=back)


scr.exitonclick()