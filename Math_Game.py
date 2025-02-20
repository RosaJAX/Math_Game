import random

def generate_question(level):
    if level == 'easy':
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 99)
    elif level == 'intermediate':
        num1 = random.randint(10, 999)
        num2 = random.randint(100, 9999)
    elif level == 'hard':
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 99999)
    else:
        return None, None, None

    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)  # Evaluate the expression
    return question, answer

def math_game():
    print("Welcome to the Math Game!")
    print("Choose a difficulty level:")
    print("1. Easy")
    print("2. Intermediate")
    print("3. Hard")

    level_choice = input("Enter the number of your choice: ")

    if level_choice == '1':
        level = 'easy'
    elif level_choice == '2':
        level = 'intermediate'
    elif level_choice == '3':
        level = 'hard'
    else:
        print("Invalid choice. Exiting game.")
        return
    
    try:
        num_questions = int(input("Enter the number of questions you want to play: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    score = 0
    for _ in range(num_questions):  # Number of questions as chosen by the user
        question, answer = generate_question(level)
        if question is None:
            print("Error generating question. Exiting game.")
            return

        print(f"Solve: {question}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {answer}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"Game over! Your final score is: {score}/{num_questions}")
    
    # Feedback based on the score
    percentage = (score / num_questions) * 100
    if percentage == 100:
        print("🎉 Congratulations! You got a perfect score! 🎉")
    elif 50 <= percentage < 100:
        print("👍 Good job! You did well!")
    else:
        print("😐 Keep practicing! You can do better!")

if __name__ == "__main__":
    math_game()
