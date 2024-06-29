from turtle import Turtle 
ALLIGNMENT = "center"
FONT = ("Arial",24,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("Desktop/PYTHON COURSE 100days/programs/turtle/snake_org/h.txt",mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"POINT: {self.score}  HIGH SCORE : {self.highscore}",align=ALLIGNMENT,font=FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Desktop/PYTHON COURSE 100days/programs/turtle/snake_org/h.txt",mode = "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.update_score()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()




