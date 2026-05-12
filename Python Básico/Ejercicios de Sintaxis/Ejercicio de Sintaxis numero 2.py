"""Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor."""

name = input("Ingrese su nombre")
last_name = input("Ingrese su apellido")
age = int(input("Ingrese su edad"))
life_stage = None

if (0<= age < 7 ):
    print("Bebé")
elif(7<= age < 10):
    print("Niño")
elif(10<= age < 13):
    print("Preadolescente")
elif(13<= age < 15):
    print("Adolescente")
elif (15 <= age < 25):
    print("Adulto joven")
elif (25 <= age < 60):
    print("Adulto")
else:
    print("Adulto mayor")