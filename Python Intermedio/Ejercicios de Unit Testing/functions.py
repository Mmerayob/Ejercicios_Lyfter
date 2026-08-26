"""3. Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos)."""

def sum_list (list):
    sum_numbers = 0
    for index in list:
        sum_numbers = sum_numbers + index
    return sum_numbers
    

"""4. Cree una función que le dé la vuelta a un string y lo retorne."""

def reverse_string (my_string):
    new_phrase = ""
    for char in range (len(my_string)-1,-1,-1):
        new_phrase += my_string[char]
    return new_phrase


"""5. Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string."""
def print_lower_upper_number_strings (string):
    lower_string = 0
    upper_string = 0
    for char in string:
        if char.isupper():
            upper_string += 1
        elif char.islower():
            lower_string += 1
    print("Hay",upper_string, "letras mayúsculas y",lower_string,"letras minúsculas.")


"""6. Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable” """

def print_phrase_sorted_alphabetically (string):

    new_list = sorted(string.split("-"))
    new_phrase = "-".join(new_list)

    return new_phrase


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


if __name__ == '__main__':
    result = sum_list([4, 6, 2, 29])
    print("El resultado de la suma de la lista es:", result)

    print(reverse_string("Hola mundo"))

    print(print_phrase_sorted_alphabetically("python-variable-funcion-computadora-monitor"))

    print(create_new_list([1, 4, 6, 7, 13, 9, 67]))