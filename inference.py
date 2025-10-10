import clips

class Inference:
    def __init__(self):
        self.env = clips.Environment()
        self.env.load("chicken_template.clp")

    def run_inference(self, symptoms):
        for symptom, value in symptoms.items():
            if value:
                self.env.assert_string(f"(symptom {symptom})")

        self.env.run()

        diagnosis = "No specific disease detected."
        recommendation = "Please provide more symptoms for an accurate diagnosis."

        for fact in self.env.facts():
            if fact.template.name == "diagnosis":
                diagnosis = fact["disease"]
            elif fact.template.name == "recommendation":
                recommendation = fact["advice"]

        return diagnosis, recommendation
