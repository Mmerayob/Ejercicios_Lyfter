# Cree un decorador que se encargue de revisar si todos los parámetros 
# de la función que decore son números, y arroje una excepción de no ser así.

def numbers_validation(func):
    def wrapper(*args):

        for num in args:
            if not isinstance(num,(int,float)):
                raise TypeError("Todos los parámetros deben ser números.")              

        return func(*args)

    return wrapper

@numbers_validation
def sum_numbers(a,b):
    return a+b

try:
    print(sum_numbers(5,2))
    print(sum_numbers(5,"dos"))
except TypeError as error:
    print(f"Error: {error}")