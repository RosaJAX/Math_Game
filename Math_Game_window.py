import random
import tkinter as tk

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
        return None, None

    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)  # Evaluate the expression
    return question, answer

def show_level_selection(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Welcome to the Math Game!").pack()
    tk.Label(root, text="Choose a difficulty level:").pack()

    levels = ["Easy", "Intermediate", "Hard"]
    level_var = tk.StringVar(value="easy")
    for level in levels:
        tk.Radiobutton(root, text=level, variable=level_var, value=level.lower()).pack(anchor=tk.W)
    
    def confirm_level():
        show_question_entry(root, level_var.get())

    tk.Button(root, text="Next", command=confirm_level).pack()

def show_question_entry(root, level):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Enter number of questions").pack()
    question_entry = tk.Entry(root)
    question_entry.pack()
    question_entry.bind("<Return>", lambda event: start_game())
    question_entry.focus_set()  # Set focus on the entry box

    def start_game():
        try:
            global total_questions
            total_questions = int(question_entry.get())
            if total_questions <= 0:
                raise ValueError
            show_game(root, level, total_questions)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid number of questions! Please enter a valid number.")

    tk.Button(root, text="Start Game", command=start_game).pack()

def show_game(root, level, num_questions):
    for widget in root.winfo_children():
        widget.destroy()

    global score, total_questions, remaining_questions, current_answer, entry, submit_button, question_label, score_label, remaining_questions_label
    score = 0
    total_questions = num_questions

    question_label = tk.Label(root, text="")
    question_label.pack()

    score_label = tk.Label(root, text=f"Score: {score}/{num_questions}")
    score_label.pack()

    entry = tk.Entry(root)
    entry.pack()
    entry.bind("<Return>", lambda event: submit_answer(level))
    entry.focus_set()  # Set focus on the entry box

    submit_button = tk.Button(root, text="Submit", command=lambda: submit_answer(level))
    submit_button.pack()

    remaining_questions_label = tk.Label(root, text=f"Questions remaining: {num_questions}")
    remaining_questions_label.pack()

    remaining_questions = num_questions
    question, current_answer = generate_question(level)
    question_label.config(text=f"Solve: {question}")

def submit_answer(level):
    global score, remaining_questions, current_answer, total_questions

    try:
        user_answer = int(entry.get())
        if user_answer == current_answer:
            score += 1
        entry.delete(0, tk.END)
    except ValueError:
        pass

    score_label.config(text=f"Score: {score}/{total_questions}")

    remaining_questions -= 1

    if remaining_questions == 0:
        final_message()
    else:
        question, current_answer = generate_question(level)
        question_label.config(text=f"Solve: {question}")
        remaining_questions_label.config(text=f"Questions remaining: {remaining_questions}")
        entry.focus_set()  # Set focus back on the entry box

def final_message():
    for widget in root.winfo_children():
        widget.destroy()

    percentage = (score / total_questions) * 100
    result_message = ""
    if percentage == 100:
        result_message = "🎉 Congratulations! You got a perfect score! 🎉"
    elif 50 <= percentage < 100:
        result_message = "👍 Good job! You did well!"
    else:
        result_message = "😐 Keep practicing! You can do better!"

    final_label = tk.Label(root, text=result_message, font=("Helvetica", 16))
    final_label.pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack()

    play_again_button = tk.Button(button_frame, text="Play Again", command=lambda: show_level_selection(root))
    play_again_button.pack(side=tk.LEFT, padx=10)

    exit_button = tk.Button(button_frame, text="Exit", command=root.destroy)  # Properly close the Tkinter window
    exit_button.pack(side=tk.LEFT, padx=10)

def math_game():
    global root
    root = tk.Tk()
    root.title("Math Game")
    root.geometry("800x600")  # Quadrupling the window size
    show_level_selection(root)
    root.mainloop()

if __name__ == "__main__":
    math_game()
