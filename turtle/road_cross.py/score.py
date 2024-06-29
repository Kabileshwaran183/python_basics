from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_score()      
    def update_score(self):
        self.goto(-210,260)
        self.write(f"LEVEL : {self.score}" , align = "center",font = FONT)     
    def increase_level(self):        
        self.score += 1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME 0VER",align = "center",font = FONT)
        
    
