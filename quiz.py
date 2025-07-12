import tkinter as tk
from tkinter import messagebox
import random
import os
from google import Image, ImageTk

class FlagQuiz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guess the Flag Quiz")
        self.window.geometry("600x500")
        self.window.configure(bg='#f0f0f0')

        # Quiz data - country names and their flag colors (simplified representation)
        self.countries = {
            "USA": {"colors": ["Red", "White", "Blue"], "description": "Stars and Stripes"},
            "UK": {"colors": ["Red", "White", "Blue"], "description": "Union Jack"},
            "France": {"colors": ["Blue", "White", "Red"], "description": "Tricolore"},
            "Germany": {"colors": ["Black", "Red", "Gold"], "description": "Tricolor"},
            "Italy": {"colors": ["Green", "White", "Red"], "description": "Tricolor"},
            "Japan": {"colors": ["White", "Red"], "description": "Rising Sun"},
            "Canada": {"colors": ["Red", "White"], "description": "Maple Leaf"},
            "Brazil": {"colors": ["Green", "Yellow", "Blue"], "description": "Green with yellow diamond"},
            "Australia": {"colors": ["Blue", "Red", "White"], "description": "Southern Cross"},
            "India": {"colors": ["Saffron", "White", "Green"], "description": "Tricolor with wheel"}
        }

        self.current_question = 0
        self.score = 0
        self.total_questions = 5
        self.questions = []

        self.create_widgets()
        self.generate_questions()
        self.show_question()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.window, text="Guess the Flag Quiz", 
                              font=("Arial", 24, "bold"), bg='#f0f0f0')
        title_label.pack(pady=20)

        # Score display
        self.score_label = tk.Label(self.window, text="Score: 0/0", 
                                   font=("Arial", 16), bg='#f0f0f0')
        self.score_label.pack(pady=10)

        # Question frame
        self.question_frame = tk.Frame(self.window, bg='#f0f0f0')
        self.question_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Question text
        self.question_label = tk.Label(self.question_frame, text="", 
                                      font=("Arial", 14), bg='#f0f0f0', wraplength=500)
        self.question_label.pack(pady=10)

        # Flag description
        self.flag_description = tk.Label(self.question_frame, text="", 
                                       font=("Arial", 12), bg='#f0f0f0', fg='#666666')
        self.flag_description.pack(pady=5)

        # Answer buttons frame
        self.answers_frame = tk.Frame(self.question_frame, bg='#f0f0f0')
        self.answers_frame.pack(pady=20)

        # Create answer buttons
        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.answers_frame, text="", 
                             font=("Arial", 12), width=20, height=2,
                             command=lambda x=i: self.check_answer(x))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        # Next button
        self.next_button = tk.Button(self.window, text="Next Question", 
                                   font=("Arial", 14), command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.config(state="disabled")

    def generate_questions(self):
        country_list = list(self.countries.keys())
        self.questions = []
        
        for _ in range(self.total_questions):
            # Select a random country
            correct_country = random.choice(country_list)
            
            # Generate 3 wrong answers
            wrong_answers = [c for c in country_list if c != correct_country]
            wrong_answers = random.sample(wrong_answers, 3)
            
            # Create answer options
            answers = [correct_country] + wrong_answers
            random.shuffle(answers)
            
            self.questions.append({
                'country': correct_country,
                'answers': answers,
                'correct_index': answers.index(correct_country)
            })

    def show_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            country = question['country']
            
            # Update question text
            self.question_label.config(text=f"Question {self.current_question + 1}: What country does this flag belong to?")
            
            # Update flag description
            flag_info = self.countries[country]
            self.flag_description.config(text=f"Flag colors: {', '.join(flag_info['colors'])}\nDescription: {flag_info['description']}")
            
            # Update answer buttons
            for i, button in enumerate(self.answer_buttons):
                button.config(text=question['answers'][i], state="normal")
            
            # Reset button colors
            for button in self.answer_buttons:
                button.config(bg='SystemButtonFace')
            
            self.next_button.config(state="disabled")

    def check_answer(self, button_index):
        question = self.questions[self.current_question]
        correct = button_index == question['correct_index']
        
        if correct:
            self.score += 1
            self.answer_buttons[button_index].config(bg='green')
        else:
            self.answer_buttons[button_index].config(bg='red')
            self.answer_buttons[question['correct_index']].config(bg='green')
        
        # Disable all buttons
        for button in self.answer_buttons:
            button.config(state="disabled")
        
        # Update score
        self.score_label.config(text=f"Score: {self.score}/{self.current_question + 1}")
        
        # Enable next button
        self.next_button.config(state="normal")

    def next_question(self):
        self.current_question += 1
        
        if self.current_question < self.total_questions:
            self.show_question()
        else:
            self.show_final_results()

    def show_final_results(self):
        # Clear the window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Show results
        result_text = f"Quiz Complete!\n\nFinal Score: {self.score}/{self.total_questions}\n"
        percentage = (self.score / self.total_questions) * 100
        
        if percentage >= 80:
            result_text += "Excellent! You're a flag expert!"
        elif percentage >= 60:
            result_text += "Good job! You know your flags well!"
        elif percentage >= 40:
            result_text += "Not bad! Keep learning about flags!"
        else:
            result_text += "Keep practicing! You'll get better!"
        
        result_label = tk.Label(self.window, text=result_text, 
                               font=("Arial", 16), bg='#f0f0f0', justify="center")
        result_label.pack(expand=True)
        
        # Restart button
        restart_button = tk.Button(self.window, text="Play Again", 
                                 font=("Arial", 14), command=self.restart_quiz)
        restart_button.pack(pady=20)

    def restart_quiz(self):
        self.window.destroy()
        FlagQuiz()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    quiz = FlagQuiz()
    quiz.run()