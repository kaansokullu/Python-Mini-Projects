from turtle import Turtle

class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(5)

        self.penup()        
        self.goto(-500, 298)
        self.pendown()

        self.borderline()
        
        self.penup()
        self.home()
        self.pendown()

        self.centerline_up()

        self.penup()
        self.home()
        self.pendown()

        self.centerline_down()

    def borderline(self):
        self.forward(990)
        self.right(90)
        self.forward(589)
        self.right(90)
        self.forward(988)
        self.right(90)
        self.forward(590)

    def centerline_up(self):
        self.setheading(90)
        self.forward(7.5)

        for _ in range(10):
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(15)

    def centerline_down(self):
        self.setheading(270)
        self.forward(7.5)

        for _ in range(10):
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(15)