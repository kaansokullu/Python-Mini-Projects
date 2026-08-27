from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVING_DISTANCE = 10
ENDING_POSITION = -300   

class Obstacle():
    def __init__(self):
        self.obstacles = []
        self.beginning_obstacle()

    def create_obstacle(self):
        new_obstacle = Turtle()
        new_obstacle.shape("square")
        new_obstacle.shapesize(stretch_wid=1, stretch_len=2)
        new_obstacle.color(self.random_color())
        new_obstacle.penup()
        new_obstacle.setheading(180)
        self.obstacles.append(new_obstacle)
        return new_obstacle

    def beginning_obstacle(self):
        for i in range(random.randint(10, 25)):
            new_obstacle = self.create_obstacle()
            new_obstacle.goto(self.random_starting_position())

    def add_obstacle(self):
        if random.randint(1, 100) < 10:
            number_of_obstacles = random.randint(1, 3)

            for _ in range(number_of_obstacles):
                new_obstacle = self.create_obstacle()
                new_obstacle.goto(self.random_position())

    def move(self):
        for obstacle in self.obstacles[:]:
            obstacle.forward(MOVING_DISTANCE)

            if obstacle.xcor() < ENDING_POSITION:
                obstacle.hideturtle()
                self.obstacles.remove(obstacle)

    def random_color(self):
        return random.choice(COLORS)

    def random_starting_position(self):
        x = random.randint(-250, 300)
        y = random.randint(-200, 250)
        return (x, y)

    def random_position(self):
        x = 300
        y = random.randint(-200, 250)
        return (x, y)

    def speed_up(self):
        global MOVING_DISTANCE
        MOVING_DISTANCE += 2