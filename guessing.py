import random

# Creating the game function
def guess_game():
    print("****** Welcome to my Guessing Game! ******\n")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    # Generating the  secret number which is between the lower_bond and the upper_bond
    secret_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    max_attempts = 5
    
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < lower_bound or guess > upper_bound:
                print(f"\nPlease guess a number between {lower_bound} and {upper_bound}.\n")
                continue
            
            if guess < secret_number:
                print("\nToo low! Try again.\n")
            elif guess > secret_number:
                print("\nToo high! Try again.\n")
            else:
                print(f"\nCongratulations! You've guessed the number {secret_number} in {attempts} attempts!\n")
                break
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
    
    if attempts == max_attempts:
        print(f"\nSorry, you've used all your attempts. The number was {secret_number}.\n")

# Run the guessing game if this code is executed directly
if __name__ == "__main__":
    guess_game()
