def trivia_quiz():
    # Define a dictionary with trivia questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "What is 5 + 7?": "12",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the smallest planet in our solar system?": "Mercury",
        "What year did the Titanic sink?": "1912"
    }

    # Iterate through the questions dictionary
    for question, correct_answer in questions.items():
        print(question)  # Display the question
        user_answer = input("Your answer: ").strip()  # Prompt user for their answer

        # Check if the user's answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Well done.\n")  # Feedback for correct answer
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")  # Feedback for incorrect answer

    print("Thanks for playing the trivia quiz!")  # Farewell message

# Run the trivia quiz
trivia_quiz()
