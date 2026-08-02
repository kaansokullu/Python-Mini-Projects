from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

        self.can_change_direction = True

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_part(pos)

    def add_part(self, pos):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(pos)
        self.snake_parts.append(new_snake)

    def extend(self):
        self.add_part(self.snake_parts[-1].position())

    def move(self):
        reversed_lst = list(reversed(self.snake_parts))
        for index in range(len(reversed_lst) - 1):
            reversed_lst[index].goto(reversed_lst[index + 1].position())

        self.head.forward(MOVING_DISTANCE)

        self.can_change_direction = True

    def will_hit_border(self):
        next_x = self.head.xcor()
        next_y = self.head.ycor()

        heading = self.head.heading()
        if heading == 0:
            next_x += MOVING_DISTANCE
        elif heading == 180:
            next_x -= MOVING_DISTANCE
        elif heading == 90:
            next_y += MOVING_DISTANCE
        elif heading == 270:
            next_y -= MOVING_DISTANCE

        return abs(next_x) > 290 or abs(next_y) > 290

    def will_hit_tail(self):
        for parts in self.snake_parts[2:]:
            if self.head.distance(parts) < 10:
                return True
        return False

    def move_up(self):
        if self.can_change_direction and self.snake_parts[0].heading() != 270:
            self.head.setheading(90)
            self.can_change_direction = False

    def move_down(self):
        if self.can_change_direction and self.head.heading() != 90:
            self.head.setheading(270)
            self.can_change_direction = False

    def move_left(self):
        if self.can_change_direction and self.head.heading() != 0:
            self.head.setheading(180)
            self.can_change_direction = False

    def move_right(self):
        if self.can_change_direction and self.head.heading() != 180:
            self.head.setheading(0)
            self.can_change_direction = False