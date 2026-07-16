import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["rock", "paper", "scissors"]

bot = random.choice(choices)
you = input("Rock, Paper, Scissors: ").lower()

print("\n_____ YOUR CHOICE _____")
if you == "rock":
    print(rock)
elif you == "paper":
    print(paper)
elif you == "scissors":
    print(scissors)

print("\n_____ BOT'S CHOICE _____")

if bot == "rock":
    print(rock)
elif bot == "paper":
    print(paper)
elif bot == "scissors":
    print(scissors)

if you == bot:
    print("DRAW")
elif you == "rock":
    if bot == "paper":
        print("YOU LOSE")
    elif bot == "scissors":
        print("YOU WIN")
elif you == "paper":
    if bot == "scissors":
        print("YOU LOSE")
    elif bot == "rock":
        print("YOU WIN")
elif you == "scissors":
    if bot == "rock":
        print("YOU LOSE")
    elif bot == "paper":
        print("YOU WIN")