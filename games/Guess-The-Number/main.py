import guess_the_number_art
import random

def difficulty(choice):
    while choice not in ["easy", "hard"]:
        print("Invalid entry! Please try again.")
        choice = input("Type 'easy' for 10 lives or type 'hard' for 5 lives: ").lower()

    if choice == "easy":
        total_lives = 10
        print("You have choosen 'easy' difficulty.")
    elif choice == "hard":
        total_lives = 5
        print("You have choosen 'hard' difficulty.")

    return total_lives
    
def num_ctrl(number):
    while True:
        try:
            number = int(number)
            return number
        except ValueError:
            print("Invalid entry! Please try again by entering a number.")
            number = input("Enter a number: ")

def play():
    print(guess_the_number_art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    remaining_lives = difficulty(input("Choose a difficulty. Type 'easy' for 10 lives or type 'hard' for 5 lives: ").lower())
    rng = random.randint(1, 100)

    while remaining_lives > 0:
        print(f"You have {remaining_lives} lives left to guess the number.")
        player_guess = num_ctrl(input("Make a guess: "))

        if player_guess == rng:
            break
        else:
            if player_guess < rng:
                print("Too low.")
            else:
                print("Too high.")
            remaining_lives -= 1

    if remaining_lives > 0:
        print(f"You got it! The answer was {rng}.")
    else:
        print(f"You've run out of guesses. The answer was {rng}. Refresh the page to run again.")

while input("Do you want to play a number guessing game? Type 'y' to play the game: ").lower() == 'y':
    play()