from turtle import Turtle


class Collison(Turtle):
    def __init__(self):
        super().__init__()

    def collison_msg(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(font=("Arial", 18, "normal"),
                   arg="Game Over Baby!!💣", align="center")

