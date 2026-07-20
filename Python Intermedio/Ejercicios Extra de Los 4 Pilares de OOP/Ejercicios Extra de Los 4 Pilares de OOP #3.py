# Cree una clase base Vehicle con los atributos:
# _brand
# _year
# Agregue un método get_info() que devuelva una descripción del vehículo.
# Luego cree dos clases hijas:
# Car
# Motorcycle
# Cada una debe agregar su propio atributo (por ejemplo, doors o type)
# y sobrescribir el método get_info() para incluir esta información adicional.

class Vehicle:
    def __init__(self,brand,year):
        self._brand = brand
        self._year = year
    
    def get_info(self):
        return f"{self._brand} ({self._year})"
    

class Car(Vehicle):
    def __init__(self, brand, year,doors):
        super().__init__(brand, year)

        self.doors = doors

    def get_info(self):
        return f"{super().get_info()} - {self.doors} puertas"
    
class Motorcycle(Vehicle):
    def __init__(self, brand, year,type):
        super().__init__(brand, year)
        self.type = type
    
    def get_info(self):
        return f"{super().get_info()} - Tipo: {self.type}"


vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

print(vehicle1.get_info())
print(vehicle2.get_info())

        
        