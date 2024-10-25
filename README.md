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

