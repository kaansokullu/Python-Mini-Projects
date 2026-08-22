from turtle import Screen
from game_field import Field
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_field = Field()
right_paddle = Paddle((450, 0))
left_paddle = Paddle((-460, 0))
ball = Ball()

move_right_paddle_up = False
move_right_paddle_down = False
move_left_paddle_up = False
move_left_paddle_down = False

def press_right_up():
	global move_right_paddle_up
	move_right_paddle_up = True

def release_right_up():
	global move_right_paddle_up
	move_right_paddle_up = False

def press_right_down():
	global move_right_paddle_down
	move_right_paddle_down = True

def release_right_down():
	global move_right_paddle_down
	move_right_paddle_down = False

def press_left_up():
	global move_left_paddle_up
	move_left_paddle_up = True

def release_left_up():
	global move_left_paddle_up
	move_left_paddle_up = False

def press_left_down():
	global move_left_paddle_down
	move_left_paddle_down = True

def release_left_down():
	global move_left_paddle_down
	move_left_paddle_down = False

screen.update()

screen.listen()

screen.onkeypress(press_right_up, "Up")
screen.onkeyrelease(release_right_up, "Up")
screen.onkeypress(press_right_down, "Down")
screen.onkeyrelease(release_right_down, "Down")
screen.onkeypress(press_left_up, "w")
screen.onkeyrelease(release_left_up, "w")
screen.onkeypress(press_left_down, "s")
screen.onkeyrelease(release_left_down, "s")

def game_loop():
    if move_right_paddle_up:
        right_paddle.move_up()
    if move_right_paddle_down:
        right_paddle.move_down()
    if move_left_paddle_up:
        left_paddle.move_up()
    if move_left_paddle_down:
        left_paddle.move_down()

    ball.ball_move()

    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()

screen.exitonclick()