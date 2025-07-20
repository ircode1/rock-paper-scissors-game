import random  # Importing the random module to let the computer make random choices

# Function to get choices from the player and the computer
def get_choices():
    # Asking the user to enter rock, paper, or scissors and converting it to lowercase
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    # Defining possible options for the computer
    options = ["rock", "paper", "scissors"]

    # Randomly selecting a choice for the computer
    computer_choice = random.choice(options)

    # Creating a dictionary to store both choices
    choices = {"player": player_choice, "computer": computer_choice}
    return choices  # Returning the dictionary

# Function to check who wins
def check_winner(player, computer):
    # Printing what the player and computer chose
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}\n")

    # If both choices are the same, it's a tie
    if player == computer:
        return "It's a tie!"

    # Conditions when player chooses rock
    elif player == "rock":
        if computer == "scissors":
            return "Rock crushes scissors! You win!"  # Rock beats scissors
        else:
            return "Paper covers rock! You lose!"     # Paper beats rock

    # Conditions when player chooses paper
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose!"

    # Conditions when player chooses scissors
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else:
            return "Rock crushes scissors! You lose!"

    else:
        # If the user enters something invalid
        return "Invalid input. Please choose rock, paper, or scissors."

# 🔁 Main game loop using while to repeat the game
while True:
    # Get the player's and computer's choices
    choices = get_choices()

    # Check who won the game
    result = check_winner(choices["player"], choices["computer"])

    # Print the result
    print(result)

    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    # If the user doesn't want to continue, break the loop
    if play_again != "yes":
        print("Thanks for playing! Goodbye! 👋")
        break  # Exit the while loop






    

