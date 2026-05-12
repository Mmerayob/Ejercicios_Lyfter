#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_songs_file (path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            # Decidí usar el método "for line in line" porque si uso "readlines()" tendría que recorrer la lista y quitar los saltos de línea uno por uno
            content = [line.strip() for line in file if line.strip()]
            sorted_list = sort_songs_list (content)
        return sorted_list
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no existe.")
        return []

def sort_songs_list (songs_list):
    return sorted(songs_list, key=str.lower)

def write_new_songs_file(path,text):

    if not text:
        print("No hay canciones para guardar.")
        return
    else:
        print("El nuevo archivo con las canciones ordenadas alfabéticamente ha sido guardado en la carpeta actual.")
    
    with open (path, 'w', encoding='utf-8') as file:
        file.write("\n".join(text))

def main():

    songs = read_songs_file('Canciones.txt')
    write_new_songs_file("canciones_ordenadas.txt",songs)

if __name__ == "__main__":
    main()