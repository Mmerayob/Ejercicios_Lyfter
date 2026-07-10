# Cree una clase abstracta de Shape que:
# 1. Tenga los métodos abstractos de calculate_perimeter y calculate_area.
# 
# Ahora cree las siguientes clases que hereden de Shape e implementen 
# esos métodos: Circle, Square y Rectangle.
# 
# Cada una de estas necesitará los atributos correspondientes (como radio, 
# lado, o base y altura) para poder realizar los cálculos.

import math

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter (self):
        pass

    @abstractmethod
    def calculate_area (self):
        pass

class Circle(Shape):
    
    def __init__(self,radio):
        self.radio = radio
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radio

    def calculate_area(self):
        return math.pi * (self.radio ** 2)
    
class Square(Shape):
    
    def __init__(self,side):
        self.side = side
    
    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2
    
class Rectangle(Shape):
    
    def __init__(self,width, length):
        self.width = width
        self.length = length
    
    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.length

    def calculate_area(self):
        return self.width * self.length
    
