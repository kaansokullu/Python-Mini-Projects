from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVING_DISTANCE = 10
DISTANCE_THRESHOLD = 22
FINISH_LINE_Y = 270

class GameIcon(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVING_DISTANCE)

    def collision_with_obstacle(self, obstacles):
        for obstacle in obstacles:
            if self.distance(obstacle) < DISTANCE_THRESHOLD:
                return True
        return False

    def reach_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)