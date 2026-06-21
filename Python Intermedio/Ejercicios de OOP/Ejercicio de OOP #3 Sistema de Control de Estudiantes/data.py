import csv
from actions import (Student)

def read_students_grades(file_path):
    student_list = []
    try:
        with open(file_path, 'r', encoding='utf-8-sig', newline='') as file:
            reader = csv.DictReader(file)      

            for student in reader:
                try:
                    new_student = Student(
                        student["Nombre completo"].strip(),
                        student["Sección"].strip(),
                        float(student["Nota de español"]),
                        float(student["Nota de inglés"]),
                        float(student["Nota de sociales"]),
                        float(student["Nota de ciencias"])
                    )
                    
                    student_list.append(new_student)
                    
                except ValueError as e:
                    print(f"Error [ValueError]: No se pudo convertir el valor de las notas ingresadas a un número.")

        print("El archivo se leyó correctamente.")
        return student_list   

    except FileNotFoundError as e:
        print(f"Error [FileNotFoundError]: El archivo {file_path} no fue encontrado. Detalles: {e}")
        return []

    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []


def write_students_grades(file_path,students):

    headers = ["Nombre completo", "Sección", "Nota de español", "Nota de inglés", "Nota de sociales", "Nota de ciencias"]

    try:

        with open(file_path,'w',encoding='utf-8-sig',newline='') as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    "Nombre completo": student.name,
                    "Sección": student.group,
                    "Nota de español": student.spanish_grade,
                    "Nota de inglés": student.english_grade,
                    "Nota de sociales": student.social_studies_grade,
                    "Nota de ciencias": student.science_grade,
                })
        
        print(f"El archivo '{file_path}' ha sido creado correctamente.")

    except Exception as e:
        print(f"Error al crear el archivo: {e}")