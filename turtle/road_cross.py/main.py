import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Score()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
i=4
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i%4==0 :
        car.new_car()
    car.move()
    for c in car.car[0:]:
        if player.distance(c)<18:
            game_is_on = False
            score.game_over()

    if player.ycor()>270:
        score.increase_level()
        player.refresh()
        car.inc_speed()
    i+=1

screen.exitonclick()