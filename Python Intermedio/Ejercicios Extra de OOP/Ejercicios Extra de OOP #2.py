# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"

class Animal:
    def __init__(self,name):
        self.name = name 

    def speak(self):
        return("Hace un sonido")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return("Guau")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return ("Miau")


my_dog = Dog("Max")
my_cat = Cat("Felix")

print(my_dog.speak())
print(my_cat.speak())