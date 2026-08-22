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

can_bounce_right_paddle = True
can_bounce_left_paddle = True

ball_is_moving = False

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

def start_game():
    global ball_is_moving
    ball_is_moving = True

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

screen.onkey(start_game, "space")

def game_loop():
    global can_bounce_right_paddle, can_bounce_left_paddle
    
    if move_right_paddle_up:
        right_paddle.move_up()
    if move_right_paddle_down:
        right_paddle.move_down()
    if move_left_paddle_up:
        left_paddle.move_up()
    if move_left_paddle_down:
        left_paddle.move_down()

    if ball_is_moving:
        ball.ball_move()

    if not (-280 <= ball.ycor() <= 280):
        ball.bounce_y()

    if can_bounce_right_paddle and ball.distance(right_paddle) < 50 and ball.xcor() > 430:
        ball.bounce_x()
        can_bounce_right_paddle = False
        can_bounce_left_paddle = True
    if can_bounce_left_paddle and ball.distance(left_paddle) < 50 and ball.xcor() < -440:
        ball.bounce_x()
        can_bounce_left_paddle = False
        can_bounce_right_paddle = True

    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()

screen.exitonclick()