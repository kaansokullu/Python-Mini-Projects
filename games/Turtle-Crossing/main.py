from turtle import Screen
from game_icon import GameIcon
from obstacle import Obstacle
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

turtle_icon = GameIcon()
obstacle = Obstacle()
score = Scoreboard()

def game_loop():
    screen.update()
    obstacle.move()
    obstacle.add_obstacle()

    if turtle_icon.collision_with_obstacle(obstacle.obstacles):
        score.game_over()
        return
    
    if turtle_icon.reach_finish_line():
        score.increase_score()
        turtle_icon.reset_position()
        obstacle.speed_up()
        
    screen.ontimer(game_loop, 20)

screen.listen()

screen.onkeypress(turtle_icon.move, "Up")

game_loop()

screen.exitonclick()