from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        self.score=0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(align="center", arg=f"Score : {self.score}", font=("Arial", 18, "normal"))
    def inc_score(self):
        self.score+=1
        self.clear()
        self.write(align="center", arg=f"Score : {self.score}", font=("Arial", 18, "normal"))

