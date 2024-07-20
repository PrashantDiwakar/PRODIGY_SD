import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Guess the number between 1 and 100")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)
        
        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess < self.number_to_guess:
                self.feedback_label.config(text="Too low! Try again.")
            elif user_guess > self.number_to_guess:
                self.feedback_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the number {self.number_to_guess} correctly in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="Invalid input. Please enter a valid number.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")


root = tk.Tk()


game = GuessingGame(root)

root.mainloop()
