from turtle import  Screen
import time
from snake import Snake
from food import Food
from score import Score

BORDERS = [-280, 280]

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

my_screen.listen()

my_screen.onkey(snake.move_up, "Up")
my_screen.onkey(snake.move_down, "Down")
my_screen.onkey(snake.move_left, "Left")
my_screen.onkey(snake.move_right, "Right")

motion_speed = 0.15

while True:
    my_screen.update()
    time.sleep(motion_speed)

    if snake.will_hit_border():
        break

    snake.move()

    if snake.head.distance(food) < 15:
        food.placement(snake.snake_parts)
        snake.extend()
        score.score_increase()
        motion_speed = max(0.05, motion_speed - 0.0025)

    if snake.will_hit_tail():
        break

score.game_over()
        

my_screen.exitonclick()