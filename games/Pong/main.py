from turtle import Screen
from game_field import Field

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_field = Field()

screen.update()

screen.exitonclick()