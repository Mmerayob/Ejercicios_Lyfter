import csv

def read_students_grades(file_path):

    student_list = []
    try:
        with open (file_path, 'r', encoding='utf-8-sig',newline='') as file:
            reader = csv.DictReader(file)      

            for student in reader:
                student_list.append({
                    "name": student["Nombre completo"].strip(),
                    "group": student["Sección"].strip(),
                    "spanish_grade": float(student["Nota de español"]),
                    "english_grade": float(student["Nota de inglés"]),
                    "social_studies_grade": float(student["Nota de sociales"]),
                    "science_grade": float(student["Nota de ciencias"]),
                })
        print("El archivo se leyó correctamente.")

    except FileNotFoundError as e:
        print(f"Error [FileNotFoundError]: El archivo {file_path} no fue encontrado. Detalles: {e}")
        print("Cerrando el programa...")
        exit()
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

    return student_list


def write_students_grades(file_path,students):

    headers = ["Nombre completo", "Sección", "Nota de español", "Nota de inglés", "Nota de sociales", "Nota de ciencias"]

    try:

        with open(file_path,'w',encoding='utf-8-sig',newline='') as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    "Nombre completo": student["name"],
                    "Sección": student["group"],
                    "Nota de español": student["spanish_grade"],
                    "Nota de inglés": student["english_grade"],
                    "Nota de sociales": student["social_studies_grade"],
                    "Nota de ciencias": student["science_grade"],
                })
        
        print(f"El archivo '{file_path}' ha sido creado correctamente.")

    except Exception as e:
        print(f"Error al crear el archivo: {e}")