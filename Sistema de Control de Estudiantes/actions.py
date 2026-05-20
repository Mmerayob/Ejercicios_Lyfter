
def add_new_student(students):

    exit_loop = False

    while not exit_loop :

        name = is_valid_name()
        group = is_valid_group ()
        spanish_grade = request_grade ("español")
        english_grade = request_grade ("inglés")
        social_studies_grade = request_grade ("sociales")
        science_grade = request_grade ("ciencias")


        student_list = {
            "name" : name,
            "group" : group,
            "spanish_grade" : spanish_grade,
            "english_grade" : english_grade,
            "social_studies_grade" : social_studies_grade,
            "science_grade" : science_grade
                }

        students.append(student_list)

        option = input("\n¿Desea agregar otro estudiante? (s/n): ").lower()
        if option == 'n':
            exit_loop = True


def request_grade (subject):

    while True:
        try:
            grade = float(input(f"Ingrese la nota de {subject}: "))
            if grade < 0 or grade > 100:
                print("La nota ingresada debe ser un número entre 0 y 100.\n"
                    "Inténtelo de nuevo.")
            else:
                return grade
            
        except ValueError as e:
            print(f"Error [ValueError]: No se pudo convertir el valor de las notas ingresadas a un número. Detalles: {e} ")


def is_valid_name ():
    
    while True:
        name = input("Ingrese el nombre completo del estudiante: ").strip()

        if not name:
            print("El nombre no puede quedar vacío. Ingrese un nombre válido para el estudiante.")
        elif any(char.isdigit() for char in name):
            print("El nombre no puede tener números. Intente nuevamente.")
        else:
            return name


def is_valid_group():

    # Como el ejercicio no específicaba a detalle el rango de grupos tomé como supuesto que
    # los grupos están entre el grado 1 y 11, además que solo existe 'A', 'B', 'C', 'D' por número.

    valid_letters = ['A', 'B', 'C', 'D']

    while True:
        group = input("Ingrese la sección del estudiante (Ej: 10A): ").upper()
        
        grade_part = group[:-1]
        letter_part = group[-1]

        if letter_part not in valid_letters:
            print("Error: La letra debe ser A, B, C o D. Intentelo de nuevo.")
            continue

        if not grade_part.isdigit():
            print("Error: La primera parte debe ser un número entero. Intentelo de nuevo.")
            continue

        number = int(grade_part)
        if not (1 <= number <= 11):
            print("Error: El grado debe estar entre 1 y 11. Intentelo de nuevo.")
            continue

        return group


def display_student_list(student_list):
    for student in student_list:
        print(f"Nombre: {student['name']}")
        print(f"Sección: {student['group']}")
        print(f"Nota de español: {student['spanish_grade']}")
        print(f"Nota de inglés: {student['english_grade']}")
        print(f"Nota de sociales: {student['social_studies_grade']}")
        print(f"Nota de ciencias: {student['science_grade']}")
        print("--------------------------------------------------------")


def add_average_student_grades (student_list):

    average_students = student_list #Nueva lista que incluye el promedio de las notas

    for student in average_students:
        total = (student["spanish_grade"] + 
                student["english_grade"] + 
                student["social_studies_grade"] + 
                student["science_grade"])
        student["average"] = total / 4

    return average_students


def display_top3_average_student_grades (student_list):

    average_students = add_average_student_grades(student_list)

    average_students.sort(key=lambda x: x["average"], reverse = True)

    for i, student in enumerate(average_students[:3], start=1):
        
        print(f"Puesto {i}: {student['name']}")
        print(f"Sección: {student['group']}")
        print(f"Nota Promedio: {student['average']}")
        print("--------------------------------------")


def display_average_student_grades (student_list):

    average_students = add_average_student_grades(student_list)

    for student in average_students:
        
        print(f"Nombre:: {student['name']}")
        print(f"Sección: {student['group']}")
        print(f"Nota Promedio: {student['average']}")
        print("--------------------------------------")


def display_failed_grades(student_list):

    for student in student_list:
        if (student['spanish_grade'] < 60 or
            student['english_grade'] < 60 or
            student['social_studies_grade'] < 60 or
            student['science_grade'] < 60):

            print("--------------------------------------") 
            print(f"Nombre: {student['name']}")
            print(f"Sección: {student['group']}")
            print("Materias reprobadas:")

            if student['spanish_grade'] < 60:
                print(f"    Nota de español: {student['spanish_grade']}")
                
            if student['english_grade'] < 60:
                print(f"    Nota de inglés: {student['english_grade']}")
                
            if student['social_studies_grade'] < 60:
                print(f"    Nota de sociales: {student['social_studies_grade']}")
                
            if student['science_grade'] < 60:
                print(f"    Nota de ciencias: {student['science_grade']}")


def remove_student_from_list(student_list):

    search_student = is_valid_name()
    search_group = is_valid_group()

    for student in student_list:
        if student['name'] == search_student and student['group'] == search_group:
            print(f"¿Está seguro que quiere eliminar al estudiante {student['name']} de la lista?. ")
            option = input("S/N").upper().strip()
            if option == "S":
                student_list.remove(student)
                print(F"El estudiante {student['name']} ha sido eliminado con exito.")
            else:
                print("El estudiante NO ha sido eliminado.")
            return

    print("No se encontró ningún estudiante con ese nombre y sección.")