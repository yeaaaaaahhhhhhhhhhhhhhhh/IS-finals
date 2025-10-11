(deftemplate symptom
   (slot name))

(deftemplate diagnosis
   (slot disease))

(deftemplate recommendation
   (slot advice))

; RULES 

(defrule InfectiousBronchitis
   (symptom (name cough))
   (symptom (name sneeze))
   (symptom (name swollen_eyes))
   =>
   (assert (diagnosis (disease "Infectious Bronchitis")))
   (assert (recommendation (advice "Provide antibiotics such as Tylosin or Doxycycline. Keep the coop warm, dry, and well-ventilated."))))

(defrule NewcastleDisease
   (symptom (name paralysis))
   (symptom (name diarrhea))
   (symptom (name sudden_death))
   =>
   (assert (diagnosis (disease "Newcastle Disease")))
   (assert (recommendation (advice "Isolate affected chickens. Provide multivitamins, clean the coop, and apply disinfectant. Vaccination is recommended."))))

(defrule FowlCholera
   (symptom (name loss_appetite))
   (symptom (name diarrhea))
   (symptom (name swollen_eyes))
   =>
   (assert (diagnosis (disease "Fowl Cholera")))
   (assert (recommendation (advice "Administer Sulfadimethoxine or Tetracycline. Ensure access to clean water and proper sanitation."))))

(defrule NoDiseaseFound
   (not (diagnosis (disease ?)))
   =>
   (assert (diagnosis (disease "Unknown Disease")))
   (assert (recommendation (advice "Consult a licensed veterinarian for further examination."))))
