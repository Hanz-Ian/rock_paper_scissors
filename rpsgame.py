# Import the random to make the computer pick random choices
import random

# Create the list of choices
choices = ["rock", "paper", "scissors"]

# Initialize the computer to pick from the choices list
computer = random.choice(choices)

# Initialize the player first before putting it in the loop
player = None


# Create a loop for when a player is picking something else other than the elements in choices
while player not in choices:
    player = input("Rock, paper, or scissors?: ").lower() # lower() to match the lowercase elements in choices


# Logic for when both players picked the same choice
if player == computer:
    print("computer: ", computer)
    print("player: ", player)
    print("It's a tie!")

# Logics for when player picks rock
elif player == "rock":
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("Paper beats rock, you lose!")

    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("Rock beats scissors, you win!")

# Logics for when player picks paper
elif player == "paper":
    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("Scissors beats paper, you lose!")

    if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("Paper beats rock, you win!")

# Logics for when player picks scissors
elif player == "scissors":
    if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("Rock beats scissors, you lose!")

    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("Scissors beats paper, you win!")
