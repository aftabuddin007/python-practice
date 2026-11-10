import random

def guess_the_number():
    print("--- Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random integer between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 7
    
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        
        # Use try-except to handle invalid input (like typing text instead of a number)
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue
            
        # Check if the guess is within bounds
        if guess < 1 or guess > 100:
            print("Keep your guess between 1 and 100.")
            continue
            
        # Compare the guess to the target number
        if guess == target_number:
            print(f"🎉 Congratulations! You guessed the number {target_number} correctly!")
            break
        elif guess < target_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
            
        # Deduct an attempt for a wrong guess
        attempts -= 1
        
    # If the loop ends because attempts reached 0
    if attempts == 0:
        print(f"\nGame Over! The number I was thinking of was {target_number}.")

if __name__ == "__main__":
    guess_the_number()