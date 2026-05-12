"""Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero."""

import random

random_number = random.randint(1,10)
selected_number = None

while random_number != selected_number:
    selected_number = int(input("Adivine el numero entre seleccionado entre 1 y 10"))
    if random_number != selected_number:
        print("No adivinó el número, intente de nuevo.")
print(f"Felicidades, el número correcto era {selected_number}.")
