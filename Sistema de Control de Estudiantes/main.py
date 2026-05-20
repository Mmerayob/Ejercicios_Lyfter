from data import read_students_grades, write_students_grades
from menu import menu

def main():

    route = input("Ingrese el nombre del archivo csv que quiere leer.")
    specific_route = route + ".csv"
    students = read_students_grades(specific_route)
    menu(students)
    write_students_grades(specific_route,students)

if __name__ == "__main__":
    main()