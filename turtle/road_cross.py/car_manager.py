from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
x=300
all_pos = []
for y in range(-250,250,20):
    pos = (x,y)
    all_pos.append(pos)
print(all_pos)

class CarManager():
    def __init__(self):
        self.car = []
        self.speed = 5
        
    def new_car(self):
        tim = Turtle("square")
        tim.shapesize(1,2)
        tim.color(random.choice(COLORS))
        tim.penup()
        tim.setheading(180)
        tim.goto(random.choice(all_pos))
        self.car.append(tim)
        self.head = tim.heading()
        self.move()
    def move(self):
        for c in self.car:
            c.forward(self.speed)
    def inc_speed(self):
        self.speed += 3
        self.move()
    




