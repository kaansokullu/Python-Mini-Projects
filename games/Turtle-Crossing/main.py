from turtle import Screen
from game_icon import GameIcon

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

turtle_icon = GameIcon()

screen.update()
screen.tracer(1)

screen.listen()

screen.onkeypress(turtle_icon.move, "Up")

screen.exitonclick()