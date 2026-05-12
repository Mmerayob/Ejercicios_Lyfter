# Dada n cantidad de notas de un estudiante, calcular:
# Cuantas notas tiene aprobadas (mayor a 70).
# Cuantas notas tiene desaprobadas (menor a 70).
# El promedio de todas.
# El promedio de las aprobadas.
# El promedio de las desaprobadas.

passed_grades = 0
failed_grades = 0
average_passed_grades = 0
average_failed_grades = 0
average_total_grades = 0
grades_count = 1
grades_total = int(input("indique la cantidad de notas que desea ingresar"))

while grades_count <= grades_total:
    grade = int(input("indique la nota que desea ingresar"))
    if(grade<70):
        failed_grades += 1; average_failed_grades = average_failed_grades + grade
    else: passed_grades += 1; average_passed_grades = average_passed_grades + grade
    grades_count += 1
    average_total_grades = average_total_grades + (grade / grades_total)

print(f"El promedio total de notas es {average_total_grades}.")

if(passed_grades > 0):
    average_passed_grades = average_passed_grades / passed_grades
    print (f"El estudiante tiene {passed_grades} notas aprobadas.")
    print(f"El promedio de notas aprobadas es {average_passed_grades}")
else: print("No hay notas aprobadas.")

if(failed_grades > 0):
    average_failed_grades =  average_failed_grades / failed_grades
    print (f"El estudiante tiene {failed_grades} notas desaprobadas.")
    print(f"El promedio de notas desaprobadas es {average_failed_grades}. ")
else: print("No hay notas desaprobadas.")