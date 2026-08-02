from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Press Start 2P", 13, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.clear()
        self.score += 1
        self.score_update()