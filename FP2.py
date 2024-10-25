import random

def generate_powerball_numbers():
    # Greeting message
    print("Welcome to the PowerBall Number Generator!")
    print("This program will generate your lottery numbers for you.")

    # Generate five white ball numbers (1-69)
    white_balls = random.sample(range(1, 70), 5)
    # Generate one red ball number (1-26)
    red_ball = random.randint(1, 26)

    # Sort the white ball numbers for better readability
    white_balls.sort()

    # Print the generated numbers with specified formatting
    print("Your PowerBall numbers are:")
    print(" ".join(map(str, white_balls)) + "   " + str(red_ball))

    # Farewell message
    print("\nGood luck with your lottery ticket!")

# Run the PowerBall number generator
generate_powerball_numbers()
