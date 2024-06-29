from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('coral')
i = True
k = 50
while i == True :
    timmy.forward(k)
    timmy.right(90)
    timmy.speed(10)
    k += 5
    
m = Screen()
m.exitonclick()
