#Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
#Lea cada línea usando csv.reader()
#Muestre el contenido en pantalla de forma legible, línea por línea
#Pida al usuario una clasificación ESRB (por ejemplo: "T")
#Muestre todos los videojuegos que tengan esa clasificación
#Cuente cuántos videojuegos hay de cada género
#Muestre el resultado de forma ordenada
#Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
#Muestre todos los videojuegos desarrollados por esa empresa en formato legible

import csv

def read_games (file_path):

    with open (file_path, 'r', encoding='utf-8-sig',newline='') as file:
        reader = csv.DictReader(file)      
        games_list = []

        for game in reader:
            games_list.append({
                "name": game["Nombre"].strip(),
                "genre": game["Género"].strip(),
                "developer": game["Desarrollador"].strip(),
                "rating": game["Clasificación ESRB"].strip(),
            })
    return games_list


def display_games (games_list):
    for game in games_list:
        print(f"Nombre: {game['name']}")
        print(f"Género: {game['genre']}")
        print(f"Desarrollador: {game['developer']}")
        print(f"Clasificación: {game['rating']}")
        print()


def display_games_by_clasification (games_list):

    while True:
        try:
            opt = input("Ingrese la clasificación ESRB del videojuego:\n  1. E (Todos)\n  2. E10+ (Mayores 10)\n  3. T (Adolescentes)\n  4. M (Maduros 17+)\n  5. AO (Sólo Adultos 18+)")

            match int(opt):
                case 1: game_clasification = "E"
                case 2: game_clasification = "E10+"
                case 3: game_clasification = "T"
                case 4: game_clasification = "M"
                case 5: game_clasification = "AO"
                case _: 
                    print("Debe elegir una opción entre 1 y 5.") 
                    continue
            break

        except ValueError as e:
                print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")

    print("---------------------------------------------------------------------")
    print("Los juegos de la lista con clasificación ",game_clasification,"son:")
    print("---------------------------------------------------------------------")

    for game in games_list:
        if game_clasification == game['rating']:
            print(f"Nombre: {game['name']}")
            print(f"Género: {game['genre']}")
            print(f"Desarrollador: {game['developer']}")
            print(f"Clasificación: {game['rating']}")
            print()


def count_game_genre(games_list):

    genres = {}

    for game in games_list:
        genres[game['genre']] = genres.get(game['genre'], 0) + 1
    
    genres_sorted = sorted(genres.items())
    
    print("----------------------------------")
    print("Cantidad de juegos por género:")
    print("----------------------------------")
    for genres,quantity in genres_sorted:
        print(genres,":",quantity)    


def display_games_by_developer(games_list):
        
    game_developer = input("Ingrese el nombre del desarrollador de videojuegos que quiere mostar.")
    print("-------------------------------------------------")
    print("Los juegos de la lista desarrollados por",game_developer,"son:")
    print("-------------------------------------------------")
    for game in games_list:
        if game_developer == game['developer']:
            print(f"Nombre: {game['name']}")
            print(f"Género: {game['genre']}")
            print(f"Desarrollador: {game['developer']}")
            print(f"Clasificación: {game['rating']}")
            print()


def main():

    route = input("Ingrese el nombre del archivo csv que quiere leer.")
    specific_route = route + ".csv"
    games = read_games(specific_route)
    display_games(games)
    display_games_by_clasification(games)
    count_game_genre(games)
    display_games_by_developer(games)

if __name__ == "__main__":
    main()