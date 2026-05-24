from actions import (add_new_student, display_student_list, display_average_student_grades,
                     display_top3_average_student_grades,display_failed_grades,remove_student_from_list)
from data import read_students_grades, write_students_grades

def menu(students):
    while True:
        try:
            opt = input("-------------------------------------------------------------------\n"
                        "             Menu de Sistema de Control de Estudiantes\n"
                        "-------------------------------------------------------------------\n"
                        "   1. Ingresar información de estudiantes.\n"  
                        "   2. Ver información de estudiantes ingresados.\n"  
                        "   3. Ver top 3 de estudiantes con mejor nota promedio.\n"  
                        "   4. Ver la nota promedio entre todos los estudiantes.\n"  
                        "   5. Eliminar un estudiante.\n"
                        "   6. Ver estudiantes reprobados.\n"
                        "   7. Importar estudiantes desde un archivo CSV.\n"
                        "   8. Exportar estudiantes a un archivo CSV.\n"
                        "   9. Salir.\n\n"
                        "Seleccione una opción: ")
            
            match int(opt):
                case 1: add_new_student (students)
                case 2: display_student_list (students)
                case 3: display_top3_average_student_grades(students)
                case 4: display_average_student_grades (students)
                case 5: remove_student_from_list(students)
                case 6: display_failed_grades(students) 
                case 7: 
                    route = input("Ingrese el nombre del archivo CSV que quiere leer (sin .csv): ").strip()
                    if route:
                        imported_data = read_students_grades(route + ".csv")
                        students.extend(imported_data)
                case 8:
                    if not students:
                        print("No hay estudiantes registrados en el sistema para exportar.")
                        continue
                    route = input("Ingrese el nombre con el que desea guardar el CSV (sin .csv): ").strip()
                    if route:
                        write_students_grades(route + ".csv", students)
                case 9: break
                case _:
                    print("Debe elegir una opción entre 1 y 9.") 
                    
        except ValueError as e:
                print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")
