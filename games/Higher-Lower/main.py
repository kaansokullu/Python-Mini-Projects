import random
import higher_lower_art
import game_data

def person_info(data_dict):
    return f"{data_dict["name"]}, a {data_dict["description"]}, from {data_dict["country"]}."


def vs_message(data_A, data_B):
    return f"""
Compare A: {person_info(data_A)}
{higher_lower_art.vs}
Against B: {person_info(data_B)}
"""

def compare(decision, data_A, data_B):
    if data_A["follower_count"] > data_B["follower_count"]:
        greater = "A"
    else:
        greater = "B"

    return decision.upper() == greater

def play():
    print(higher_lower_art.logo)
    info_A = random.choice(game_data.data)
    info_B = random.choice(game_data.data)
    score = 0

    while True:
        print(vs_message(info_A, info_B))
        player_choice = input("Who has more followers? Type 'A' or 'B': ")
        if compare(player_choice, info_A, info_B):
            score += 1
            print("\n"*30)
        else:
            break

        info_A = info_B
        info_B = random.choice(game_data.data)
        print(higher_lower_art.logo)
        print(f"You're right! Current score: {score}")
        
    print(higher_lower_art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

play()