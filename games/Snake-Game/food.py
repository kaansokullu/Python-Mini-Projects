from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)

        self.placement([])

    def placement(self, snake_parts):
        while True:
            rng_x_cor = random.randint(-14, 14) * 20
            rng_y_cor = random.randint(-14, 14) * 20

            is_on_snake = False
            for parts in snake_parts:
                if parts.distance(rng_x_cor, rng_y_cor) < 15:
                    is_on_snake = True
                    break

            if not is_on_snake:
                self.teleport(rng_x_cor, rng_y_cor)
                break