from turtle import Turtle, Screen

REMAINING_TIME = 600

class Countdown:
    def __init__(self, game_screen):
        self.time_left = REMAINING_TIME
        self.screen = game_screen
        self.timer_display = Turtle()
        self.timer_display.hideturtle()
        self.timer_display.penup()
        self.timer_display.teleport(-485, -250)
        self.time_is_running = True
        self.update_timer()
        self.decrease_time()

    def update_timer(self):
        self.timer_display.clear()
        self.timer_display.write(f"{self.convert_time(self.time_left)}", align="left", font=("Times New Roman", 30, "normal"))

    def convert_time(self, given_time):
        minutes = given_time // 60
        seconds = given_time % 60
        return f"{minutes:02d}:{seconds:02d}"

    def decrease_time(self):
        if self.time_is_running and self.time_left > 0:
            self.time_left -= 1
            self.update_timer()
            self.screen.ontimer(self.decrease_time, 1000)
        else:
            self.time_is_running = False
            self.update_timer()

    def stop_timer(self):
        self.time_is_running = False