"""Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados."""

name = "Manfred"
last_name = "Merayo"
number_int = 7
number_float = 8.5
completed = True
pending = True
new = False
grades_list = [100, 80, 75]
students_list = ["Manfred", "Jose", "Alex"]

print (name + " " + last_name)

"""Cuando intenté sumar string + int me dio error porque no se pueden sumar estos tipos de datos"""
"""print(name + number_int)"""

"""cuando intenté sumar int + string me dio error porque no se pueden sumar estos tipos de datos"""
"""print(number_int + name)"""

print(grades_list + students_list)

"""cuando intenté concatenar string + list me dio error porque no se pueden sumar estos tipos de datos"""
"""print(name + grades_list)"""

print(number_int + number_float)
print(pending + completed)
print (pending + new)

"""para los booleanos toma el valor de True como 1 y el valor de False como 0"""
