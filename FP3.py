import random

def number_guessing_game():
    # Greeting message
    print("Welcome to the Number Guessing Game!")
    play_game = input("Do you want to play? (yes/no): ").strip().lower()

    # Check if the user wants to play
    if play_game == "no":
        print("Maybe next time!")
        return  # End the program

    elif play_game == "yes":
        # Generate a secret number between 1 and 10
        secret_number = random.randint(1, 10)

        # Loop until the user guesses the correct number
        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))

                if guess == secret_number:
                    print("Congratulations! You've guessed the number!")
                    break  # Exit the loop when guessed correctly
                else:
                    print("Try again!")  # Prompt the user to guess again

            except ValueError:
                print("Please enter a valid number between 1 and 10.")

    # Farewell message
    print("Thank you for playing! Goodbye!")

# Run the number guessing game
number_guessing_game()
