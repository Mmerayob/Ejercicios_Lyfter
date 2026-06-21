# Cree una clase de Circle con:
#   Un atributo de radius (radio).
#   Un método de get_area que retorne su área.

import math

class Circle:
    
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * (self.radius * self.radius)
        return area

circle_1 = Circle(2)

print(f"El área del círculo es {circle_1.get_area():.2f}")


