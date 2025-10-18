import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from inference import Inference

class ChickenExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Chicken Disease Expert System")
        self.root.geometry("800x1000")
        self.client_data = {}
        self.vet_answers = {}
        self.user_symptoms = {}
        self.inference_engine = Inference()

        
        self.vet_questions = [
            "What are the most common poultry diseases you usually encounter?",
            "What are the primary symptoms for each disease?",
            "Which symptoms should be prioritized during early detection?",
            "What treatments and medications are recommended for each disease?",
            "How can farmers prevent the spread of these diseases?",
            "How important is vaccination in poultry health?"
        ]

        
        self.user_questions = {
            "cough": "Is the chicken having difficulty breathing?",
            "swollen_eyes": "Do the chickens have watery eyes or nasal discharge?",
            "loss_appetite": "Are the feathers ruffled or is there loss of appetite?",
            "diarrhea": "Is there bloody diarrhea?",
            "paralysis": "Do you observe paralysis or twisting of the neck?"
        }

        self.show_client_form()

    
    def show_client_form(self):
        self.clear_window()
        tk.Label(self.root, text="🐔 Chicken Disease Expert System", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Label(self.root, text="Enter Client Information", font=("Arial", 14)).pack(pady=10)

        self.entry_name = self.create_input("Client Name:")
        self.entry_farm = self.create_input("Poultry Farm Name:")
        self.entry_address = self.create_input("Address:")
        self.entry_date = self.create_input("Date (leave blank for today):")

        tk.Button(self.root, text="Proceed to Vet Assessment", font=("Arial", 12),
                  command=self.start_assessment).pack(pady=20)

    def create_input(self, label):
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Label(frame, text=label, width=20, anchor="w").pack(side="left")
        entry = tk.Entry(frame, width=40)
        entry.pack(side="left")
        return entry

    def start_assessment(self):
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

        self.show_vet_questions()

    
    def show_vet_questions(self):
        self.clear_window()
        tk.Label(self.root, text="Veterinarian Assessment", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.root, text="Please answer the questions below:", font=("Arial", 12)).pack(pady=5)

        self.vet_textboxes = []
        for q in self.vet_questions:
            frame = tk.Frame(self.root)
            frame.pack(pady=10)
            tk.Label(frame, text=q, font=("Arial", 12), anchor="w", justify="left", wraplength=700).pack(anchor="w")
            txt = tk.Text(frame, height=3, width=80, font=("Arial", 11), wrap="word")
            txt.pack()
            self.vet_textboxes.append((q, txt))

        tk.Button(self.root, text="Proceed to User Questions", font=("Arial", 14, "bold"),
                  bg="blue", fg="white", command=self.save_vet_and_show_user).pack(pady=30)

    def save_vet_and_show_user(self):
        
        self.vet_answers.clear()
        for q, txt in self.vet_textboxes:
            self.vet_answers[q] = txt.get("1.0", "end-1c").strip()

        self.show_user_questions()

    
    def show_user_questions(self):
        self.clear_window()
        tk.Label(self.root, text="Farmer/Client Assessment", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.root, text="Answer Yes or No to the questions below:", font=("Arial", 12)).pack(pady=5)

        self.user_vars = {}
        for key, question in self.user_questions.items():
            frame = tk.Frame(self.root)
            frame.pack(anchor="w", pady=5)
            tk.Label(frame, text=question, font=("Arial", 12), wraplength=700, justify="left").pack(side="left", padx=10)
            var = tk.StringVar(value="No")
            tk.Radiobutton(frame, text="Yes", variable=var, value="Yes").pack(side="left")
            tk.Radiobutton(frame, text="No", variable=var, value="No").pack(side="left")
            self.user_vars[key] = var

        tk.Button(self.root, text="Submit Assessment", font=("Arial", 14, "bold"),
                  bg="green", fg="white", command=self.submit_assessment).pack(pady=30)

    
    def submit_assessment(self):
        
        for key, var in self.user_vars.items():
            self.user_symptoms[key] = True if var.get() == "Yes" else False

        
        diagnosis, recommendation = self.inference_engine.run_inference(self.user_symptoms)

        
        summary = f"""Client Information
----------------------------
Client Name: {self.client_data['name']}
Poultry Farm Name: {self.client_data['farm']}
Address: {self.client_data['address']}
Date: {self.client_data['date']}

Veterinarian Assessment
----------------------------
"""
        for q, ans in self.vet_answers.items():
            summary += f"{q}\nAnswer: {ans}\n\n"

        summary += "User Symptoms\n----------------------------\n"
        for key, val in self.user_symptoms.items():
            summary += f"{self.user_questions[key]} Answer: {'Yes' if val else 'No'}\n"

        summary += f"""
Diagnosis & Recommendation
----------------------------
Diagnosis: {diagnosis}
Recommendation: {recommendation}
"""

        self.clear_window()
        tk.Label(self.root, text="Assessment Summary", font=("Arial", 18, "bold")).pack(pady=10)
        text = tk.Text(self.root, width=90, height=35, wrap="word")
        text.pack(pady=10)
        text.insert("1.0", summary)
        text.config(state="disabled")

        tk.Button(self.root, text="New Assessment", font=("Arial", 12),
                  command=self.show_client_form).pack(pady=20)

    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChickenExpertSystem(root)
    root.mainloop()
