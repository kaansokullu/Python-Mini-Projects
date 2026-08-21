from turtle import Screen
from game_field import Field
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_field = Field()
right_paddle = Paddle((450, 0))
left_paddle = Paddle((-460, 0))

screen.update()
screen.tracer(1)

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

screen.exitonclick()