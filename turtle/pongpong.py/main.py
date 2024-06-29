from turtle import *
from paddle import Paddle
from ball import Ball
from score import Score
import time
#screen
scr = Screen()
scr.screensize(800,600)
scr.bgcolor("black")
scr.title("PONG")
scr.tracer(0)
#paddle
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
#ball
ball = Ball() 
#score board
score = Score()

scr.listen()
scr.onkey(l_paddle.go_up,"w")
scr.onkey(l_paddle.go_down,"s")
scr.onkey(r_paddle.go_up,"o")
scr.onkey(r_paddle.go_down,"l")
game_on = True
while game_on :
    time.sleep(ball.move_speed) 
    scr.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380:
        score.l_point()
        ball.reposition()
    if ball.xcor()<-380:
        score.r_point()
        ball.reposition()
    #     game_on = False




scr.exitonclick()