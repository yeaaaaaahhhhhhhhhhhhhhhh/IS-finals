(deftemplate symptom
   (slot name))

(deftemplate diagnosis
   (slot disease))

(deftemplate recommendation
   (slot advice))


(defrule InfectiousBronchitis
   (or (symptom (name cough))
       (symptom (name sneeze)))
   (symptom (name swollen_eyes))
   =>
   (assert (diagnosis (disease "Infectious Bronchitis")))
   (assert (recommendation (advice "Provide antibiotics such as Tylosin or Doxycycline. Keep the coop warm, dry, and well-ventilated. Isolate sick chickens."))))


(defrule NewcastleDisease
   (or (symptom (name paralysis))
       (symptom (name twisted_neck)))
   (or (symptom (name diarrhea))
       (symptom (name greenish_droppings)))
   (or (symptom (name sudden_death))
       (symptom (name weakness)))
   =>
   (assert (diagnosis (disease "Newcastle Disease")))
   (assert (recommendation (advice "Isolate affected chickens. Provide multivitamins, clean the coop, and disinfect. Vaccinate healthy chickens immediately."))))


(defrule FowlCholera
   (symptom (name loss_appetite))
   (or (symptom (name diarrhea))
       (symptom (name greenish_droppings)))
   (or (symptom (name swollen_eyes))
       (symptom (name nasal_discharge)))
   =>
   (assert (diagnosis (disease "Fowl Cholera")))
   (assert (recommendation (advice "Administer Sulfadimethoxine or Tetracycline. Ensure access to clean water and proper sanitation. Clean the coop thoroughly."))))


(defrule InfectiousCoryza
   (symptom (name nasal_discharge))
   (symptom (name swollen_face))
   (or (symptom (name cough))
       (symptom (name sneeze)))
   =>
   (assert (diagnosis (disease "Infectious Coryza")))
   (assert (recommendation (advice "Administer Erythromycin or Sulfadimethoxine. Quarantine affected chickens and improve ventilation."))))


(defrule AvianInfluenza
   (symptom (name sudden_death))
   (symptom (name respiratory_distress))
   (or (symptom (name diarrhea))
       (symptom (name nasal_discharge)))
   =>
   (assert (diagnosis (disease "Avian Influenza")))
   (assert (recommendation (advice "This is a highly contagious disease. Immediately contact your local veterinary authority. Quarantine and disinfect thoroughly."))))


(defrule NoMatchFound
   (symptom (name ?s))
   (not (diagnosis (disease ?d)))
   =>
   (assert (diagnosis (disease "No exact match found")))
   (assert (recommendation (advice "Symptoms may indicate multiple conditions. Consult a veterinarian for accurate diagnosis."))))


(defrule NoDiseaseFound
   (not (symptom (name ?)))
   =>
   (assert (diagnosis (disease "Unknown Disease")))
   (assert (recommendation (advice "No symptoms detected. Please enter at least one symptom."))))
