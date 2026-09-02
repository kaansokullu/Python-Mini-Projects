import turtle
import pandas as pd
import score

screen = turtle.Screen()
screen.setup(width=986, height=510)
screen.bgpic("blank_turkey_map.png")

score_display = score.Score()

df = pd.read_csv("turkey_cities.csv")
df["condition"] = False

def data_check(player_input):
    if player_input in df["city"].values and not df.loc[df["city"] == player_input, "condition"].values[0]:
        df.loc[df["city"] == player_input, "condition"] = True
        return True
    else:
        return False

def mark_city(city_name):
    city_data = df[df.city == city_name]
    x_cor = int(city_data.X.iloc[0])
    y_cor = int(city_data.Y.iloc[0])
    turtle.hideturtle()
    turtle.penup()
    turtle.teleport(x_cor, y_cor)
    turtle.write(city_name, font=("Times New Roman", 13, "normal"))

while True:
    player_answer = screen.textinput(title="Guess the City", prompt="Write a city name:").title()

    if player_answer == "Istanbul":
        player_answer = "İstanbul"
    elif player_answer == "Izmir":
        player_answer = "İzmir"

    if data_check(player_answer):
        mark_city(player_answer)
        score_display.increase_score()
        
screen.exitonclick()