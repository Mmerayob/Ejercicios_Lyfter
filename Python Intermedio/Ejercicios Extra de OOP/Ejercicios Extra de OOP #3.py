# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
#   Guarde productos en una lista
#   Tenga métodos para:
#       Agregar un producto
#       Mostrar todos los productos
#       Calcular el valor total del inventario

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.product_list = []

    def add_product(self,product):
        self.product_list.append(product)
    
    def display_product(self):
        for product in self.product_list:
            print(f"Producto: {product.name}")

    def calculate_total_price(self):
        total_price = 0
        for product in self.product_list:
            total_price += (product.price * product.quantity)
        return total_price
    
my_inventory = Inventory()
product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

my_inventory.add_product(product1)
my_inventory.add_product(product2)
my_inventory.display_product()
print(f"El valor total del inventario es: {my_inventory.calculate_total_price()}")