from turtle import Turtle

class GameIcon(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0, -250)
        self.setheading(90)

    def move(self):
        self.forward(10)

    