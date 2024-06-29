from turtle import *
from snake import Snake
scr = Screen()
scr.bgcolor("black")
scr.screensize(600,600)
#create snake
snake = Snake()

game = True
while game:
    snake.move_snake()



scr.exitonclick()
