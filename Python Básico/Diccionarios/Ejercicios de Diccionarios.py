"""1. Cree un diccionario que guarde la siguiente información sobre un hotel:"""
# nombre
# numero_de_estrellas
# # habitaciones
# El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
# numero
# piso
# precio_por_noche

hotel = {
"name":"Hotel 1",
"stars_rating":5,
"rooms":[
    {
    "room_number": 5,
    "room_floor": 3,
    "prize": 25,
    },
    {
    "room_number": 17,
    "room_floor": 20,
    "prize": 35,
    }]
}
print(hotel["rooms"][1])

"""2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values"""

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

student = dict(zip(list_a,list_b))
print(student)

"""3. Cree un programa que use una lista para eliminar keys de un diccionario."""

keys_list = ["access_level", "age"]
employee = {"name":"John","email":"john@ecorp.com","access_level":5,"age":28}

for index in keys_list:
    employee.pop(index)
print(employee)