# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def sum_numbers (first_number):
    try:
        second_number = float(input("Digite el número que quiere sumar."))
        result = first_number + second_number
        print("--------------------------------------------------------")
        print(f"Resultado: {result}")
        return result
    except ValueError as e:
        print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")
        return first_number

def subtract (first_number):
    try:
        second_number = float(input("Digite el número que quiere restar."))
        result = first_number - second_number
        print("--------------------------------------------------------")
        print(f"Resultado: {result}")
        return result
    except ValueError as e:
        print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")
        return first_number

def multiply (first_number):
    try:
        second_number = float(input("Digite el número que quiere multiplicar."))
        result = first_number * second_number
        print("--------------------------------------------------------")
        print(f"Resultado: {result}")
        return result
    except ValueError as e:
        print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")
        return first_number

def division (first_number):

    try:
        second_number = float(input("Digite el número divisor."))
        result = first_number / second_number
        print("--------------------------------------------------------")
        print(f"Resultado: {result}")
        return result
    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: Intentaste dividir {first_number} entre 0. Detalles: {e}")
        return first_number
    except ValueError as e:
        print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")
        return first_number

def main():

    while True:
        try:
            first_number = float(input("Digite el primer número que desea ingresar en la calculadora."))
            break
        except ValueError as e:
            print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")

    while True:

        try:
            print("--------------------------------------------------------")
            print("1. Suma.\n2. Resta.\n3. Multiplicación\n4. División.\n5. Borrar resultado.\n6. Salir.")
            print("--------------------------------------------------------")

            option = int(input("Seleccione la opción que quiere elegir:"))

            match option:
                case 1:
                    #Suma
                    first_number = sum_numbers(first_number)
                case 2:
                    #Resta
                    first_number = subtract(first_number)
                case 3:
                    #Multiplicación
                    first_number = multiply(first_number)
                case 4:
                    #División
                    first_number = division(first_number)
                case 5:
                    #Borrar resultado
                    first_number = 0
                    print("El resultado ha sido borrado.")
                    print("--------------------------------------------------------")
                    print("Resultado: 0")
                case 6:
                    #Salir
                    break
                case _:
                    print("Debe elegir entre las opciones del menú entre 1 y 6")
        
        except ValueError as e:
            print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")

if __name__ == "__main__":
    main()