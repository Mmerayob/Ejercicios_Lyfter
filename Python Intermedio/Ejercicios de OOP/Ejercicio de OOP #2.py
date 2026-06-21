#Cree una clase de Bus con:
#   1. Un atributo de max_passengers.
#   2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la
#      clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. 
#      Sino, debe mostrar un mensaje de que el bus está lleno.
#   3. Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person:	
    def __init__(self,name):
        self.name = name

class Bus:
    def __init__(self,max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self,person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else: print("El bus ya está lleno")
    
    def remove_passanger(self,person_name):
        for passanger in self.passengers:
            if passanger.name == person_name:
                self.passengers.remove(passanger)
                return print(f"El pasajero {passanger.name} fue bajado del bus")
            
        return print(f"El pasajero {person_name} no fue encontrado dentro del bus.")


person_1 = Person("Manfred")
person_2 = Person("Maria")
bus_1 = Bus(40)

bus_1.add_passenger(person_1)
bus_1.remove_passanger("Manfred")
bus_1.remove_passanger("Juan")




