import random

winning_conditions = {
    "rock" : "scissors",
    "paper" : "rock",
    "scissors" : "paper"
}

user_name = input("Enter your name: ")

def get_user_choice():
    user_choice = input("Please enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in winning_conditions:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(list(winning_conditions.keys()))

def determine_winner(user_choice, computer_choice):
    if computer_choice == user_choice:
        return("It's a tie")

    elif winning_conditions[user_choice] == computer_choice:
        return(f"{user_name} wins")

    else:
        return("Computer wins")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"{user_name} chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again (Yes/No) ? ").lower()

        if play_again != "yes":
            break


play_game()