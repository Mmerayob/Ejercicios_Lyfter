"""1. Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar"""

my_list = [4,2,7,2,8,2,1]
searched_number = 2
found_count = 0

for index in my_list:
    if index == searched_number:
        found_count += 1
print(f"El número 2 aparece ",found_count," veces")

"""2. Cree un programa que verifique si todos los elementos de una lista son positivos"""

my_list = [3,6,0,-2,4]

for index in my_list:
    if index < 1:
        print("Hay al menos un número negativo o cero")
        break
else: print("Todos los números son positivos")

"""3. Cree un programa que muestre el valor más pequeño de una lista sin usar min()."""

my_list = [9,4,7,1,5]

min_number = my_list[0]

for index in my_list:
    if index < min_number:
        min_number = index

print(f"El valor más pequeño de la lista es ",min_number)


"""4. Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio"""

my_list = [10,20,30,40,50]
average_number = 0
count_my_list = 0
new_list = []

for index in my_list:
    average_number += index
    count_my_list += 1
average_number = average_number/count_my_list

for index in my_list:
    if index > average_number:
        new_list.append(index)

print(f"El promedio es: ",average_number)
print(f"Nueva lista: ",new_list)

"""5. Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras"""
word_list = []
new_list = []

for index in range (5):
    word = input("Digite la palabra que desea agregar a la lista.")
    word_list.append(word)
print(f"Lista original: ",word_list)

for index in word_list:
    if len(index) > 4:
        new_list.append(index)
print(f"Nueva lista con palabras de más de 4 letras: ",new_list)