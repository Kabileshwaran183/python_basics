from turtle import *
from snake import Snake
from food import Food
from score import Score
import time
# create background on turtle
scr = Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("MY SNAKE GAME")
scr.tracer(0)#for animie. because the each segment is move one after another.so next scr.update
# create snake body
snake = Snake()
# create snake food
food = Food()
# increase the score 
score = Score()

scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")
# move the snake by key
game_on = True
while game_on :
    scr.update()
    time.sleep(0.1)
    snake.move_snake()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        score.increase_score()
        print("num num num")
    # detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()
    # detect collision with tail
    for segment in snake.segment[1:] :
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()






scr.exitonclick()