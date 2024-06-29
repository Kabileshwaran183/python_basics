from turtle import Turtle,Screen
class square:
    def step(self,forward,right):
        self.f = forward
        self.r = right
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

sq = square()
for i in range(0,4):
    sq.step(timmy.forward(100),timmy.right(90))
screen = Screen()
screen.exitonclick()


