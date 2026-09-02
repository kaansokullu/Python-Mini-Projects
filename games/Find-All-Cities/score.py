from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(475, 220)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}/81", align="right", font=("Times New Roman", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()
