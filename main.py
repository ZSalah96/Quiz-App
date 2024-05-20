import tkinter as tk
import json

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        
        # Set the window size
        self.root.geometry("600x1000")

        # Load the quiz data from the JSON file
        with open('json', 'r') as file:
            self.quiz_data = json.load(file)
        
        self.questions = self.quiz_data['questions']
        self.total_questions = len(self.questions)
        self.current_question_index = 0
        self.score = 0
        self.user_answers = []  # List to store user answers and correctness

        # Create the GUI components
        self.question_label = tk.Label(root, text="", wraplength=500, justify="center")
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value="")
        self.option_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.options_var, value="", indicatoron=0, width=30)
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        # Display the first question
        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        question_text = f"Question {self.current_question_index + 1}: {question_data['question']}"
        self.question_label.config(text=question_text)
        options = question_data['options']
        self.options_var.set(None)  # Reset the selected option

        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option, value=option)

    def check_answer(self):
        selected_option = self.options_var.get()
        if selected_option:
            correct_answer = self.questions[self.current_question_index]['answer']
            is_correct = selected_option == correct_answer
            self.user_answers.append({
                'question': self.questions[self.current_question_index]['question'],
                'selected_option': selected_option,
                'correct_answer': correct_answer,
                'is_correct': is_correct
            })

            if is_correct:
                self.score += 1

            self.current_question_index += 1
            if self.current_question_index < self.total_questions:
                self.display_question()
            else:
                self.display_result()

    def display_result(self):
        self.question_label.pack_forget()
        for btn in self.option_buttons:
            btn.pack_forget()
        self.submit_button.pack_forget()

        result_text = f"Quiz completed!\nYour score: {self.score}/{self.total_questions}\n\n"
        for i, answer in enumerate(self.user_answers):
            result_text += f"Question {i + 1}: {answer['question']}\n"
            result_text += f"Your answer: {answer['selected_option']}\n"
            if answer['is_correct']:
                result_text += "Result: Correct!\n\n"
            else:
                result_text += f"Result: Incorrect! The correct answer was: {answer['correct_answer']}\n\n"

        result_label = tk.Label(self.root, text=result_text, fg="black", justify="left")
        result_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = Quiz(root)
    root.mainloop()
