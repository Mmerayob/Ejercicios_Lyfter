#Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

class Rectangle:
    
    def __init__(self,width,height):
        if (width < 0 or height < 0):
            raise ValueError("El ancho y la altura no pueden ser valores negativos")

        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter
    
my_rectangle = Rectangle(8,4)

print(f"El área del rectangulo es: {Rectangle.get_area(my_rectangle)}")

print(f"El perimetro del rectangulo es: {Rectangle.get_perimeter(my_rectangle)}")