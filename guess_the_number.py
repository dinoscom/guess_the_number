import random

name = input("Γεία σου! Παρακαλώ γράψε το όνομα σου.\n--->")
print("Ωραία! ας παίξουμε ένα παιχνίδι!")

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Μάντεψε τον αριθμό μεταξύ 1 και {x}\n"))
        if guess < random_number:
            print("Λυπάμαι, μάντεψε ξανά. Πολύ μικρός")
        elif guess > random_number:
            print("Λυπάμαι, μάντεψε ξανά. Πολύ μεγάλος")
    
    print(f"Συγχαρητήρια {name}!! Βρήκες τον κρυφό αριθμό {random_number}")

guess(50)