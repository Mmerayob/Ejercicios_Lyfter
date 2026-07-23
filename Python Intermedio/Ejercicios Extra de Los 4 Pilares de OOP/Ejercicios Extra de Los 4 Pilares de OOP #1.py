# Cree una clase Employee con los siguientes requisitos:
# Atributos privados: _name, _salary
# Use @property y @<atributo>.setter para:
# Mostrar el nombre y el salario
# Validar que el salario nunca sea negativo
# Cree un método promote que aumente el salario un porcentaje definido

class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,new_name):
        self._name = new_name
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,new_salary):
        if new_salary < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = new_salary
    
    def promote(self,percentage):
        self.salary = self.salary + ((self.salary * percentage))
        return self.salary
    

employee = Employee("Ana", 1000)
employee.promote(0.1)

print(employee.salary)
