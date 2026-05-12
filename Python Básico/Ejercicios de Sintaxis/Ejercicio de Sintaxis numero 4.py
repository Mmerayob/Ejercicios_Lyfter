# Cree un programa que le pida tres números al usuario y muestre el mayor.

first_number = float(input("Seleccione el primer número."))
second_number = float(input("Seleccione el segundo número."))
third_number = float(float(input("Seleccione el tercer número.")))

if (first_number > second_number and first_number > third_number):
    print(f"El numero mayor es {first_number}")
elif(second_number > first_number and second_number > third_number):
    print(f"El numero mayor es {second_number}")
elif(third_number > first_number and third_number > second_number):
    print(f"El numero mayor es {third_number}")
    
