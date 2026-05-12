#Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON (ipsum:lesson/python-bsico/manejo-de-json)
#Debe leer el archivo para importar los Pokémones existentes.
#Luego debe pedir la información del Pokémon a agregar.
#Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def read_pokedex_json (path):
    try:
        with open(path, 'r') as file:
            pokedex = json.load(file)
            print("¡Archivo cargado con éxito!")
        return pokedex
    except FileNotFoundError:
        print("Error: El archivo 'pokedex.json' no existe en esta carpeta.") 
        return []
    except Exception as e:
        print(f"Error al crear el archivo: {e}")


def add_new_pokemon ():

    name = input("Ingrese el nombre del nuevo pokemon.")
    type = input("Ingrese el tipo del nuevo pokemon.")
    level = int(input("Ingrese el nivel del nuevo pokemon"))
    weight = float(input("Ingrese el peso en kilogramos del nuevo pokemon"))

    shiny_ask = input("¿Es shiny? (s/n): ").lower()
    if shiny_ask == "s":
        is_shiny = True
    else:
        is_shiny = False

    held_iteam = input("Ingrese el nombre del *held item*")
    skills_input = input("Ingrese las skills separadas por coma: ")
    skills_list = skills_input.split(",")

    new_pokemon = {
        "name" : name,
        "type" : type,
        "level": level,
        "weight_kg": weight,
        "is_shiny": is_shiny,
        "held_item": held_iteam,
        "skills": skills_list
        }
    
    return new_pokemon

def write_new_pokemon (path,pokedex_list):
    try:
        with open(path, 'w') as file:
            json.dump(pokedex_list,file, indent=4)
    except Exception as e:
        print(f"Error al guardar: {e}")     

def main():

    path = input("Escriba el nombre del archivo json.")
    pokedex_list = read_pokedex_json (path)
    new = add_new_pokemon()
    pokedex_list.append(new)
    write_new_pokemon(path,pokedex_list)
  
if __name__ == "__main__":
    main()