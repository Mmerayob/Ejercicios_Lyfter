"""1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo."""

first_list = ["Hay","en","que","iteración","indices","muy"]
second_list = ["casos","los","la","por","es","útil"]

for index in range (0,len(first_list)):
    first_words = first_list[index]
    second_words = second_list[index]
    print(first_words,second_words)

"""2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda."""

my_string = "Pizza con piña"

for char in range (len(my_string)-1,-1,-1):
    print(my_string[char])

"""3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño."""

my_list = [4, 3, 6, 1, 7]
first_number = my_list[0]

print("Lista original: ",my_list)

my_list[0] = my_list[len(my_list)-1]
my_list[len(my_list)-1] = first_number

print("Lista invertida: ",my_list)

"""4. Cree un programa que elimine todos los números impares de una lista."""

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in range (len(new_list)-1,-1,-1):
    if (new_list[index] % 2) != 0:
        new_list.pop(index)

print ("Lista sin números impares: ",new_list)


"""5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto. """

numbers_list = []

for index in range (10):
    num = int(input("Digite el número que va a agregar a la lista:"))
    numbers_list.append(num)    

max_number = numbers_list[0]

for index in range (len(numbers_list)):
    if numbers_list [index] > max_number:
        max_number = numbers_list [index]

print ("La lista de números ingresados es: ",numbers_list)
print("El número más alto de esa lista es: ",max_number)