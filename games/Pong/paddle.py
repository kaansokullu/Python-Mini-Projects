from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green1")
        self.shapesize(stretch_wid=4, stretch_len=0.6)
        self.penup()
        self.goto(position)

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()

        if y_cor <= 250:
            self.goto(x_cor, y_cor + 15)

    def move_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()

        if y_cor >= -240:
            self.goto(x_cor, y_cor - 15)