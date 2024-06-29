from turtle import Turtle
STARTING_POSITION = (0, -272)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1,1)
        self.penup()
        self.setheading(90)
        self.refresh()
    def refresh(self):
        self.goto(STARTING_POSITION)
    def move(self):
        self.forward(20)


