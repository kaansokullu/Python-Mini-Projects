from turtle import Screen
from game_icon import GameIcon
from obstacle import Obstacle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

turtle_icon = GameIcon()
obstacle = Obstacle() 

def game_loop():
    screen.update()
    obstacle.move()
    obstacle.add_obstacle()
    screen.ontimer(game_loop, 20)


screen.listen()

screen.onkeypress(turtle_icon.move, "Up")

game_loop()

screen.exitonclick()