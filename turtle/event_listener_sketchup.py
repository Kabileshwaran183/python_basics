from turtle import *

tim = Turtle()
scr = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

scr.listen()
scr.onkeypress(key = "w",fun=move_forward)
scr.onkeypress(key = "s",fun = move_backward)
scr.onkeypress(key = "a",fun=turn_left)
scr.onkeypress(key = "d",fun = turn_right)
scr.onkeypress(key = "c",fun=clear)


scr.exitonclick()