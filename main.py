import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from inference import Inference


class ChickenExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Chicken Disease Expert System")
        self.root.geometry("600x500")

        self.client_data = {}
        self.questions = [
            ("Does the chicken have coughing?", "cough"),
            ("Does the chicken sneeze or have nasal discharge?", "sneeze"),
            ("Does the chicken have diarrhea or greenish droppings?", "diarrhea"),
            ("Is the chicken unable to stand or showing paralysis?", "paralysis"),
            ("Are the eyes swollen or reddish?", "swollen_eyes"),
            ("Has the chicken lost appetite or stopped eating?", "loss_appetite"),
            ("Have there been sudden deaths among chickens?", "sudden_death")
        ]

        self.answers = {}
        self.index = 0

        self.show_client_form()

    #  CLIENT FORM 
    def show_client_form(self):
        self.clear_window()

        tk.Label(self.root, text="🐔 Chicken Disease Expert System", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.root, text="Enter Client Information", font=("Arial", 14)).pack(pady=10)

        self.entry_name = self.create_input("Client Name:")
        self.entry_farm = self.create_input("Poultry Farm Name:")
        self.entry_address = self.create_input("Address:")
        self.entry_date = self.create_input("Date (leave blank for today):")

        tk.Button(self.root, text="Start Diagnosis", font=("Arial", 12), command=self.start_diagnosis).pack(pady=20)

    def create_input(self, label):
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Label(frame, text=label, width=18, anchor="w").pack(side="left")
        entry = tk.Entry(frame, width=30)
        entry.pack(side="left")
        return entry

    def start_diagnosis(self):
        name = self.entry_name.get().strip()
        farm = self.entry_farm.get().strip()
        address = self.entry_address.get().strip()
        date = self.entry_date.get().strip() or datetime.now().strftime("%Y-%m-%d")

        if not name or not farm or not address:
            messagebox.showwarning("Input Error", "Please fill in all required fields.")
            return

        self.client_data = {
            "name": name,
            "farm": farm,
            "address": address,
            "date": date
        }

        self.show_questions()

    #  QUESTIONS FOR CLIENTS 
    def show_questions(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="", font=("Arial", 16), wraplength=500)
        self.label.pack(pady=60)

        self.btn_yes = tk.Button(self.root, text="Yes", width=10, font=("Arial", 12), command=lambda: self.answer("Yes"))
        self.btn_no = tk.Button(self.root, text="No", width=10, font=("Arial", 12), command=lambda: self.answer("No"))
        self.btn_yes.pack(side="left", padx=100)
        self.btn_no.pack(side="right", padx=100)

        self.ask_question()

    def ask_question(self):
        if self.index < len(self.questions):
            question, _ = self.questions[self.index]
            self.label.config(text=question)
        else:
            self.show_result()

    def answer(self, response):
        _, fact_name = self.questions[self.index]
        self.answers[fact_name] = (response == "Yes")
        self.index += 1
        self.ask_question()

    #  RESULT
    def show_result(self):
        self.clear_window()

        inference = Inference()
        diagnosis, recommendation = inference.run_inference(self.answers)

        info = f"""
Client Name: {self.client_data['name']}
Poultry Farm: {self.client_data['farm']}
Address: {self.client_data['address']}
Date: {self.client_data['date']}
-----------------------------
Diagnosis: {diagnosis}
Recommendation: {recommendation}
"""
        tk.Label(self.root, text="Diagnosis Result", font=("Arial", 16, "bold")).pack(pady=10)
        text = tk.Text(self.root, height=15, width=70, wrap="word")
        text.pack(pady=10)
        text.insert("1.0", info)
        text.config(state="disabled")

        tk.Button(self.root, text="New Diagnosis", command=self.restart, font=("Arial", 12)).pack(pady=10)

    def restart(self):
        self.answers = {}
        self.index = 0
        self.show_client_form()

    #  UTILITY
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ChickenExpertSystem(root)
    root.mainloop()
