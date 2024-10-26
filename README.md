# FridayProject7
Emma Fontenot's repository for DS 3850 Friday Project 7

Friday Project # 1:

Mad Libs Game in Python
Description
This is a simple Mad Libs game implemented in Python. The game prompts the user for various types of words and incorporates them into a funny story template.

How It Works:
The program prompts the user to provide the following inputs:

A large object
Large objects (plural)
An adjective
A body part
A restaurant
A food
Another food
The user inputs are then inserted into a pre-defined story template, which is displayed at the end.

Code Breakdown:
def mad_lib():
    # Define a function called mad_lib that contains the game logic.
    
    print("Welcome to the Mad Libs game!")
    # Print a welcome message to the user.
    
    print("Please provide the following words:")
    # Prompt the user to prepare for inputting words.

    large_object = input("A large object: ")
    # Ask the user for a large object and store it in the variable large_object.
    
    large_objects_plural = input("Large objects (plural): ")
    # Ask the user for a plural form of a large object and store it in the variable large_objects_plural.
    
    adjective = input("An adjective: ")
    # Ask the user for an adjective and store it in the variable adjective.
    
    body_part = input("A body part: ")
    # Ask the user for a body part and store it in the variable body_part.
    
    restaurant = input("A restaurant: ")
    # Ask the user for a restaurant name and store it in the variable restaurant.
    
    first_food = input("A food: ")
    # Ask the user for a type of food and store it in the variable first_food.
    
    second_food = input("Another food: ")
    # Ask the user for another type of food and store it in the variable second_food.

    story = (
        # Start creating the story by using an f-string for string interpolation.
        f"I’ve had a very {adjective} day.\n"
        # Insert the adjective into the story.
        
        f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n"
        # Insert the plural large objects and body part into the story.
        
        f"Then, at lunch, I went to {restaurant} for their delicious {first_food},\n"
        # Insert the restaurant and first food into the story.
        
        f"But the waiter brought me {second_food}, which I was not hungry for.\n"
        # Insert the second food into the story.
        
        f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."
        # Insert the singular large object into the story.
    )

    print("\nHere’s your Mad Lib story:\n")
    # Print a message indicating the start of the story output.

    print(story)
    # Print the completed story to the console.

    # Run the mad_lib function to execute the game
    mad_lib()
    # Call the mad_lib function to start the game.

Friday Project #2:

PowerBall Number Generator
Description
This Python program generates random lottery numbers for PowerBall tickets. It selects five unique numbers from a range of 1 to 69 (white balls) and one number from a range of 1 to 26 (red ball). The program formats the output according to specified requirements.

Code
import random
Import the random module: This module is essential for generating random numbers.

def generate_powerball_numbers():
    # Greeting message
    print("Welcome to the PowerBall Number Generator!")
    print("This program will generate your lottery numbers for you.")

Define the generate_powerball_numbers function: This function encapsulates the logic for generating PowerBall numbers.
Greeting messages: Introduces the user to the program's purpose.

    # Generate five white ball numbers (1-69)
    white_balls = random.sample(range(1, 70), 5)

Generate white ball numbers: Uses random.sample to select five unique numbers from the range of 1 to 69.

    # Generate one red ball number (1-26)
    red_ball = random.randint(1, 26)

Generate the red ball number: Uses random.randint to pick one number from the range of 1 to 26.

    # Sort the white ball numbers for better readability
    white_balls.sort()

Sort the white ball numbers: This step arranges the white ball numbers in ascending order for easier readability.

    # Print the generated numbers with specified formatting
    print("Your PowerBall numbers are:")
    print(" ".join(map(str, white_balls)) + "   " + str(red_ball))

Output formatting: The white ball numbers are converted to strings and joined with a single space between them. Three spaces are included before the red ball number for the specified formatting.

    # Farewell message
    print("\nGood luck with your lottery ticket!")

Farewell message: Concludes the program with a good luck message for the user.

# Run the PowerBall number generator
generate_powerball_numbers()

Execute the function: Calls the generate_powerball_numbers function to run the program.

Friday Project #3
Number Guessing Game

Description:
This Python program is a simple number guessing game where the computer selects a secret number between 1 and 10. The user attempts to guess the number, and the program provides feedback on whether the guess is correct. The game continues until the user guesses correctly or decides to quit.

Code:

import random

Import the random module: This module is necessary for generating a random secret number.

def number_guessing_game():
    # Greeting message
    print("Welcome to the Number Guessing Game!")
    play_game = input("Do you want to play? (yes/no): ").strip().lower()

Define the number_guessing_game function: This function contains the logic for the game.
Greeting messages: Welcomes the user and asks if they want to play. The input is converted to lowercase for easier comparison.

    # Check if the user wants to play
    if play_game == "no":
        print("Maybe next time!")
        return  # End the program

User decision handling: If the user answers "no", a farewell message is printed, and the function returns, ending the program.

    elif play_game == "yes":
        # Generate a secret number between 1 and 10
        secret_number = random.randint(1, 10)

Proceed if the user wants to play: If the user answers "yes", a random integer between 1 and 10 is generated and stored as the secret number.

        # Loop until the user guesses the correct number
        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))

Start an infinite loop: The program enters a loop where it will continue asking the user to guess.
User input: The program prompts the user to enter their guess and attempts to convert it to an integer.

                if guess == secret_number:
                    print("Congratulations! You've guessed the number!")
                    break  # Exit the loop when guessed correctly

Check the guess: If the user’s guess matches the secret number, a congratulatory message is printed, and the loop is exited.

                else:
                    print("Try again!")  # Prompt the user to guess again

Incorrect guess: If the guess is incorrect, the program prompts the user to try again.

            except ValueError:
                print("Please enter a valid number between 1 and 10.")

Input validation: If the user enters a non-integer value, a ValueError is caught, and the program prompts the user to enter a valid number.

    # Farewell message
    print("Thank you for playing! Goodbye!")

Farewell message: After the user guesses correctly or quits, a thank you message is printed.

    # Run the number guessing game
    number_guessing_game()

Execute the function: The number_guessing_game function is called to start the game.

Friday Project #4

Trivia Quiz Program
Description:
This Python program is a simple trivia quiz that displays questions from a predefined dictionary. Users can input their answers, and the program provides immediate feedback on whether their answers are correct or incorrect.

Code:

def trivia_quiz():
    # Define a dictionary with trivia questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "What is 5 + 7?": "12",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the smallest planet in our solar system?": "Mercury",
        "What year did the Titanic sink?": "1912"
    }

Define the trivia_quiz function: This function contains the main logic for the trivia quiz.
Dictionary of questions: A dictionary called questions is created, where:
Keys are the trivia questions.
Values are the correct answers to those questions.

    # Iterate through the questions dictionary
    for question, correct_answer in questions.items():
        print(question)  # Display the question

Loop through the dictionary: A for loop iterates over each question and its corresponding correct answer.
Display the question: The current question is printed to the console.

        user_answer = input("Your answer: ").strip()  # Prompt user for their answer

User input: The program prompts the user to input their answer, stripping any leading or trailing whitespace

        # Check if the user's answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Well done.\n")  # Feedback for correct answer

Check the answer: The program checks if the user's answer (converted to lowercase) matches the correct answer (also converted to lowercase) to ensure case insensitivity.
Feedback for correct answer: If the answer is correct, the user receives a congratulatory message.

        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")  # Feedback for incorrect answer

Feedback for incorrect answer: If the answer is incorrect, the program informs the user of the correct answer.

    print("Thanks for playing the trivia quiz!")  # Farewell message

Farewell message: After all questions have been answered, a thank you message is displayed.

    # Run the trivia quiz
    trivia_quiz()

Execute the function: The trivia_quiz function is called to start the quiz.

Friday Project #5:

Description:
This Python program allows users to display text in different colors in the console. It defines five functions, each designed to format a string of text in a specific color. The user can also input their own text and choose the color for display.

Code:

    # ANSI escape codes for text colors
Comment: This line indicates that ANSI escape codes will be used to change the text colors in the console.

def redText(text):
    return f"\033[91m{text}\033[0m"  # Red text

Define redText function: This function takes a string input (text) and returns it formatted to display in red using the ANSI escape code \033[91m.

def blueText(text):
    return f"\033[94m{text}\033[0m"  # Blue text

Define blueText function: This function returns the input string formatted to display in blue using the ANSI escape code \033[94m.

def greenText(text):
    return f"\033[92m{text}\033[0m"  # Green text

Define greenText function: This function returns the input string formatted to display in green using the ANSI escape code \033[92m.

def yellowText(text):
    return f"\033[93m{text}\033[0m"  # Yellow text

Define yellowText function: This function returns the input string formatted to display in yellow using the ANSI escape code \033[93m.

def brownText(text):
    return f"\033[38;5;94m{text}\033[0m"  # Brown text (using extended colors)

Define brownText function: This function returns the input string formatted to display in brown using the extended color code \033[38;5;94m.

# Main program logic
def main():

Define main function: This function contains the main logic of the program.

    # Call each function and print the text in the corresponding color
    print(redText("This text is red!"))
    print(blueText("This text is blue!"))
    print(greenText("This text is green!"))
    print(yellowText("This text is yellow!"))
    print(brownText("This text is brown!"))

Demonstrate color functions: Calls each color function and prints sample text in the corresponding color.

    # User input for color choice and text
    color_choice = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()

Prompt for user input: Asks the user to choose a color and strips any leading/trailing whitespace, converting the input to lowercase.

    user_text = input("Enter the text you want to display: ")

User input for text: Prompts the user to enter the text they wish to display in the chosen color.

    # Display the user-selected color
    if color_choice == "red":
        print(redText(user_text))

Check color choice: Depending on the user's input, calls the corresponding color function to display the text in the selected color. This block continues for each color option.

    else:
        print("Invalid color choice. Please choose from red, blue, green, yellow, or brown.")

Handle invalid input: If the user inputs an invalid color, a message is displayed informing them of the valid options.

    main()

Execute the program: The main function is called to start the program when the script is run directly.
