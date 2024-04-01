import random

# Quiz questions and answers
questions = {
    "What is the capital of France?": ["Paris"],
    "Who wrote 'To Kill a Mockingbird'?": ["Harper Lee"],
    "What is the powerhouse of the cell?": ["Mitochondria"],
    "What year did the Titanic sink?": ["1912"],
    "Who painted the Mona Lisa?": ["Leonardo da Vinci"]
}

# Function to generate random quiz
def generate_quiz(questions, num_questions):
    random_questions = random.sample(list(questions.items()), num_questions)
    return random_questions

# Function to display quiz and calculate score
def display_quiz(questions):
    score = 0
    for question, answer in questions:
        user_answer = input(question + "\n")
        if user_answer.strip().lower() in answer:
            score += 1
    return score

# Main function
def main():
    print("Welcome to the Python Quiz!")

    # Generate a quiz with 3 random questions
    quiz = generate_quiz(questions, 3)

    # Display the quiz and calculate score
    score = display_quiz(quiz)

    # Display the final score
    print(f"Your final score is: {score}/3")

if __name__ == "__main__":
    main()

