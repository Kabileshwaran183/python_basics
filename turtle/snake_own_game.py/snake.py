from turtle import Turtle
seg_pos = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segment = []
        self.head = self.segment[0]
        for position in seg_pos:
            self.add_segment()

    def add_segment(self,position) :
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)  
     
    def move_snake(self):
        for seg in range(len(self.segment)-1,0,-1):
            x_pos = self.segment[seg-1].xcor()
            y_pos = self.segment[seg-1].ycor()
            self.segment[seg].goto(x_pos,y_pos)
        self.head.forward(20)




