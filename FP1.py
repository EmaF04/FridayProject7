def mad_lib():
    # Welcome the user and provide instructions
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words:")

    # Gather inputs from the user
    large_object = input("A large object: ")
    large_objects_plural = input("Large objects (plural): ")
    adjective = input("An adjective: ")
    body_part = input("A body part: ")
    restaurant = input("A restaurant: ")
    first_food = input("A food: ")
    second_food = input("Another food: ")

    # Construct the story using the inputs
    story = (
        f"I’ve had a very {adjective} day.\n"
        f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n"
        f"Then, at lunch, I went to {restaurant} for their delicious {first_food},\n"
        f"But the waiter brought me {second_food}, which I was not hungry for.\n"
        f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."
    )

    # Print the completed Mad Lib story
    print("\nHere’s your Mad Lib story:\n")
    print(story)

# Run the mad_lib function to execute the game
mad_lib()
