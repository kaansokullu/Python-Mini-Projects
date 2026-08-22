from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Press Start 2P", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(position)
        self.score_update()

    def score_update(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.clear()
        self.score += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)