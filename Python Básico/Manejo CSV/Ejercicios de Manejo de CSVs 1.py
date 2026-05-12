#Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
#Debe incluir: Nombre - Género - Desarrollador - Clasificación ESRB

import csv

def insert_videogames_list ():
    
    exit = False
    all_games = []

    while not exit :

        
        game_name = input("Ingrese el nombre del videojuego.")
        game_genre = input("Ingrese el género del videojuego.")
        game_developer = input("Ingrese el desarrollador del videojuego.")
        
        while True:
            try:
                opt = input("Ingrese la clasificación ESRB del videojuego:\n  1. E (Todos)\n  2. E10+ (Mayores 10)\n  3. T (Adolescentes)\n  4. M (Maduros 17+\n  5. AO (Sólo Adultos 18+)")

                match int(opt):
                    case 1: game_clasification = "E (Todos)"
                    case 2: game_clasification = "E10+ (Mayores 10)"
                    case 3: game_clasification = "T (Adolescentes)"
                    case 4: game_clasification = "M (Maduros 17+)"
                    case 5: game_clasification = "AO (Sólo Adultos 18+)"
                    case _: 
                        print("Debe elegir una opción entre 1 y 5.") 
                        continue
                break

            except ValueError as e:
                print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")

        videogame_list = {
                'Nombre': game_name,
                'Género': game_genre,
                'Desarrollador':game_developer,
                'Clasificación ESRB':game_clasification,
                }
            
        all_games.append(videogame_list)

        option = input("\n¿Desea agregar otro juego? (s/n): ").lower()
        if option == 'n':
            exit = True

    file_name = input("Indique como quiere nombrar al archivo csv:")
    full_file_name = file_name + ".csv"
    headers = ['Nombre', 'Género', 'Desarrollador', 'Clasificación ESRB']

    try:

        with open(full_file_name,'w',encoding='utf-8-sig',newline='') as file:
            writer = csv.DictWriter(file,headers)
            writer.writeheader()
            writer.writerows(all_games)
        
        print(f"El archivo '{full_file_name}' ha sido creado correctamente.")

    except Exception as e:
        print(f"Error al crear el archivo: {e}")

def main():

    insert_videogames_list ()

if __name__ == "__main__":
    main()
