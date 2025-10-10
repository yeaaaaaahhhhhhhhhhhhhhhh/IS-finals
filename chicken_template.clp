(deftemplate symptom
   (slot name))

(deftemplate diagnosis
   (slot disease))

(deftemplate recommendation
   (slot advice))

;  RULES 

(defrule InfectiousBronchitis
   (symptom cough)
   (symptom sneeze)
   (symptom swollen_eyes)
   =>
   (assert (diagnosis (disease "Infectious Bronchitis")))
   (assert (recommendation (advice "Provide antibiotics such as Tylosin or Doxycycline. Keep the coop warm, dry, and well-ventilated."))))

(defrule NewcastleDisease
   (symptom paralysis)
   (symptom diarrhea)
   (symptom sudden_death)
   =>
   (assert (diagnosis (disease "Newcastle Disease")))
   (assert (recommendation (advice "Isolate affected chickens. Provide multivitamins, clean the coop, and apply disinfectant. Vaccination is recommended."))))

(defrule FowlCholera
   (symptom loss_appetite)
   (symptom diarrhea)
   (symptom swollen_eyes)
   =>
   (assert (diagnosis (disease "Fowl Cholera")))
   (assert (recommendation (advice "Administer Sulfadimethoxine or Tetracycline. Ensure access to clean water and proper sanitation."))))

(defrule NoDiseaseFound
   (not (diagnosis ?))
   =>
   (assert (diagnosis (disease "Unknown Disease")))
   (assert (recommendation (advice "Consult a licensed veterinarian for further examination."))))
