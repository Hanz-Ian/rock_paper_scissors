# Import the random to make the computer pick random choices
import random

# Create the list of choices
choices = ["rock", "paper", "scissors"]

# Initialize player win counts
player_win = 0
computer_win = 0

# Initialize a boolean variable to determine the game loop
game_loop = True


# Set the game_loop so start the loop
while game_loop == True:

    # Initialize the player before putting it in the next loop (And set it to None)
    player = None

    # Initialize the computer to pick from the choices list
    computer = random.choice(choices)

    # Print the win counts
    print("\nPlayer wins:", player_win,
          "\nComputer wins:", computer_win)

    # Create a loop for when a player is picking something else other than the elements in choices
    while player not in choices:
        player = input("\nRock, paper, or scissors?: ").lower() # lower() to match the lowercase elements in choices


    # Logic for when both players picked the same choice
    if player == computer:
        print("\ncomputer: ", computer)
        print("player: ", player)
        print("\nIt's a tie!")

    # Logics for when player picks rock
    elif player == "rock":
        if computer == "paper":
            print("\ncomputer: ", computer)
            print("player: ", player)
            print("\nPaper beats rock, you lose!")
            computer_win += 1

        if computer == "scissors":
            print("\ncomputer: ", computer)
            print("player: ", player)
            print("\nRock beats scissors, you win!")
            player_win += 1

    # Logics for when player picks paper
    elif player == "paper":
        if computer == "scissors":
            print("\ncomputer: ", computer)
            print("player: ", player)
            print("\nScissors beats paper, you lose!")
            computer_win += 1

        if computer == "rock":
            print("\ncomputer: ", computer)
            print("player: ", player)
            print("\nPaper beats rock, you win!")
            player_win += 1

    # Logics for when player picks scissors
    elif player == "scissors":
        if computer == "rock":
            print("\ncomputer: ", computer)
            print("player: ", player)
            print("\nRock beats scissors, you lose!")
            computer_win += 1

        if computer == "paper":
            print("\ncomputer: ", computer)
            print("player: ", player)
            print("\nScissors beats paper, you win!")
            player_win += 1


    # Set up option for when the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

# Print the end of program
print("\nEnd of program, thanks for playing!")
