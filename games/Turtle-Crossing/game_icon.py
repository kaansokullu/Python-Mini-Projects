from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVING_DISTANCE = 10
DISTANCE_THRESHOLD = 23

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