import tkinter as tk
import json

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        
        # Load the quiz data from the JSON file
        with open('json', 'r') as file:
            self.quiz_data = json.load(file)
        
        self.questions = self.quiz_data['questions']
        self.total_questions = len(self.questions)
        self.current_question_index = 0
        self.score = 0

        # Create the GUI components
        self.question_label = tk.Label(root, text="", wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value="")
        self.option_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.options_var, value="", indicatoron=0, width=20)
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

        # Display the first question
        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data['question'])
        options = question_data['options']
        self.options_var.set(None)  

        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option, value=option)

    def check_answer(self):
        selected_option = self.options_var.get()
        if selected_option:
            correct_answer = self.questions[self.current_question_index]['answer']
            if selected_option == correct_answer:
                self.score += 1
                self.result_label.config(text="Correct!", fg="green")
            else:
                self.result_label.config(text=f"Incorrect! The correct answer was: {correct_answer}", fg="red")

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
        self.result_label.config(text=f"Quiz completed!\nYour score: {self.score}/{self.total_questions}", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = Quiz(root)
    root.mainloop()


