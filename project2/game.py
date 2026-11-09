import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    
    print("--- Rock, Paper, Scissors ---")
    print("Type 'quit' to end the game.\n")

    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
        # Exit condition
        if user_choice == 'quit':
            print(f"\nFinal Score - You: {player_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
            
        # Input validation
        if user_choice not in choices:
            print("Invalid choice. Please check your spelling and try again.\n")
            continue
            
        # Computer makes a move
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # Display current score
        print(f"Current Score - You: {player_score} | Computer: {computer_score}\n")

if __name__ == "__main__":
    play_game()