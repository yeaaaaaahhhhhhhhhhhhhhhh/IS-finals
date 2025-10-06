# IS-finals

Expert System for Chicken Diseases

Flow of the System

Step 1: Start

The user opens the program (main.py).

A Tkinter window appears asking for:

Client Name

Poultry Farm Name

Address

Date

Step 2: Begin Diagnosis

After entering client details, the system begins asking Yes/No questions such as:

“Is the chicken having difficulty breathing?”

“Do the chickens have watery eyes or nasal discharge?”

“Are the feathers ruffled or is there loss of appetite?”

“Is there bloody diarrhea?”

“Do you observe paralysis or twisting of the neck?”

Step 3: Collect Responses

Each “Yes” or “No” answer is stored as a fact in Python (example: breathing_problem = True).

Once all questions are answered, these facts are passed to the inference engine (inference.py).

Step 4: Rule Execution

The inference.py file sends all the collected facts to CLIPS (chicken_template.clp).

The CLIPS file evaluates the facts using its rule base:

Example rule:

IF breathing_problem AND nasal_discharge THEN disease = "Infectious Bronchitis"

CLIPS infers the most probable disease based on the rules.

Step 5: Generate Diagnosis

After inference, the system displays:

Disease Name (example: Infectious Bronchitis)

Recommended Action (example: "Provide antibiotics and isolate sick chickens.”)

Suggested Medication (example: “Give Amoxicillin in drinking water for 3–5 days.”)



Step 6: Display and Save Report

Client Name: Rhio Dela Cruz
Farm Name: Rhio's Poultry Farm
Address: Baka-bakahan ,Pandi Bulacan
Date: October 6, 2025

Diagnosis Result:
Disease: Newcastle Disease
Recommendation: Isolate infected chickens immediately and provide vitamin supplements.
Medication: Use Newcastle vaccine for prevention and electrolytes for support.


4. Example of Knowledge Base (Simplified Rules)

In chicken_template.clp:

(deftemplate chicken
   (slot breathing_problem)
   (slot nasal_discharge)
   (slot diarrhea)
   (slot paralysis)
   (slot appetite_loss))

(defrule newcastle-disease
   (chicken (breathing_problem yes) (nasal_discharge yes) (paralysis yes))
   =>
   (assert (diagnosis "Newcastle Disease"))
   (assert (treatment "Isolate chickens, provide vitamins, and vaccinate others."))
)

(defrule fowl-cholera
   (chicken (diarrhea yes) (breathing_problem yes))
   =>
   (assert (diagnosis "Fowl Cholera"))
   (assert (treatment "Use Sulfadimethoxine or Tetracycline; disinfect housing."))
)

5. System Output Example

When all steps are completed, the program outputs something like:

# Chicken Disease Diagnosis Report 

Client Name: Wilson Esmabe
Farm Name: Wilson's Poultry Farm
Address: Marilao, Sta.Maria
Date: October 6, 2025

Diagnosis: Fowl Cholera
Recommendation: Use Sulfadimethoxine or Tetracycline. Maintain proper sanitation.
