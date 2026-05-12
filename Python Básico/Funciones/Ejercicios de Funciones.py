"""1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda."""

def print_hello_world ():
    print("Hello",end="")
    print(" ",end="")
    print_world()

def print_world ():
    print("world")

print_hello_world ()

"""2. Experimente con el concepto de scope:
*Intente acceder a una variable definida dentro de una función desde afuera."""

def num_int ():
    example = 1

num_int()

"""Al intentar imprimir la variable desde fuera de la función se produce el NameError, porque la variable no ha sido definida en el scope correspondiente"""
print(example) 


"""*Intente acceder a una variable global desde una función y cambiar su valor."""

word = "prueba1"

def new_string ():
    # En caso de no crear word como variable global, word solo sería "prueba 2" dentro del scope de la función
    # pero como este caso es global entonces el cambio se mantiene aún afuera de la función
    global word 
    word = "prueba2"
    print(word)

new_string()
print(word)

"""3. Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos)."""

def sum_list (list):
    sum_numbers = 0
    for index in list:
        sum_numbers = sum_numbers + index
    return sum_numbers
    
result = sum_list ([4,6,2,29])
print(f"El resultado de la suma de la lista es: ",result)


"""4. Cree una función que le dé la vuelta a un string y lo retorne."""

def reverse_string (my_string):
    new_phrase = ""
    for char in range (len(my_string)-1,-1,-1):
        new_phrase += my_string[char]
    return new_phrase

print(reverse_string("Hola mundo"))

"""5. Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string."""
def print_lower_upper_number_strings (string):
    lower_string = 0
    upper_string = 0
    for char in string:
        if char.isupper():
            upper_string += 1
        elif char.islower():
            lower_string += 1
    print("Hay ",upper_string, " letras mayúsculas y ",lower_string," letras minúsculas.")

print_lower_upper_number_strings("I love Nación Sushi")

"""6. Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable” """

def print_phrase_sorted_alphabetically (string):

    new_list = sorted(string.split("-"))
    new_phrase = "-".join(new_list)

    return new_phrase

print(print_phrase_sorted_alphabetically ("python-variable-funcion-computadora-monitor"))


"""7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma."""

def validate_prime_numbers (number):

    if number < 2:
        return False
    
    for index in range(2,int(number ** 0.5)+1):
        if number % index == 0:
            return False
    return True

def create_new_list (list_numbers):
    
    new_list = []
    for number in list_numbers:
        if validate_prime_numbers (number):
            new_list.append(number)
    return new_list

print(create_new_list ([1, 4, 6, 7, 13, 9, 67]))
