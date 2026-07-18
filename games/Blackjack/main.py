import blackjack_art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def hit(deck, hand):
    hand.append(random.choice(deck))

def calculate_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    
    while 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def compare(p_score, c_score):
    print("----- WINNER -----")
    if p_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif p_score == 0:
        return "Win with a Blackjack 😎"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif p_score > c_score:
        return "You win 😀"
    elif p_score < c_score:
        return "You lose 😤"
    else:
        return "Draw 🙃"
    
def show(p_hand, c_hand):
    return f"----- CURRENT PLAY -----\nYour cards: {p_hand}, current score: {calculate_score(p_hand)}\nComputer's first card: {c_hand[0]}"

def final_show(p_hand, c_hand):
    if calculate_score(p_hand) > 21:
        return f"----- END OF THE GAME -----\nYour final hand: {p_hand}, final score: {calculate_score(p_hand)}\nComputer's final hand: {[c_hand[0]]}, final score: {c_hand[0]}\n"
    return f"----- END OF THE GAME -----\nYour final hand: {p_hand}, final score: {calculate_score(p_hand)}\nComputer's final hand: {c_hand}, final score: {calculate_score(c_hand)}\n"

def play():
    print(blackjack_art.logo)

    player_hand = random.choices(cards, k = 2)
    computer_hand = random.choices(cards, k = 2)

    print(show(player_hand, computer_hand))

    if calculate_score(player_hand) != 0:
        draw_a_card = input("\nType 'y' to get another card, type 'n' to pass: ")

        while draw_a_card == 'y':
            hit(cards, player_hand)
            print("\n" + show(player_hand, computer_hand))

            if calculate_score(player_hand) > 21:    
                break
            
            draw_a_card = input("\nType 'y' to get another card, type 'n' to pass: ")

    if calculate_score(player_hand) <= 21:
        while calculate_score(computer_hand) != 0 and calculate_score(computer_hand) < 17:
            hit(cards, computer_hand)

    print("\n" + final_show(player_hand, computer_hand))
    print(compare(calculate_score(player_hand), calculate_score(computer_hand)) + "\n")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n"*50)
    play()