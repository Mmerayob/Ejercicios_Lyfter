from actions import add_new_student, display_student_list, display_average_student_grades,display_top3_average_student_grades,display_failed_grades,remove_student_from_list

def menu(students):
    while True:
        try:
            opt = input("-------------------------------------------------------------------\n"
                        "             Menu de Sistema de Control de Estudiantes\n"
                        "-------------------------------------------------------------------\n"
                        "   1. Ingresar información de estudiantes.\n"  
                        "   2. Ver información de estudiantes ingresados.\n"  
                        "   3. Ver top 3 de estudiantes con mejor nota promedio.\n"  
                        "   4. Ver la nota promedio entre las notas de todos los estudiantes.\n"  
                        "   5. Eliminar un estudiante.\n"
                        "   6. Ver estudiantes reprobados.\n"
                        "   7. Salir.\n\n"
                        "Seleccione una opción: ")
            
            match int(opt):
                case 1: add_new_student (students)
                case 2: display_student_list (students)
                case 3: display_top3_average_student_grades(students)
                case 4: display_average_student_grades (students)
                case 5: remove_student_from_list(students)
                case 6: display_failed_grades(students) 
                case 7: break
                case _:
                    print("Debe elegir una opción entre 1 y 7.") 
                    
        except ValueError as e:
                print(f"Error [ValueError]: No se pudo convertir el valor ingresado a un número. Detalles: {e} ")
