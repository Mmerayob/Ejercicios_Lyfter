# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

class Product:
    def __init__(self,price):
        self.price = price

def register_IVA(func):
    def wrapper(product):

        print(f"El precio del producto antes del IVA es: {product.price}")
            
        result = func(product)

        print(f"El monto del IVA es {result}")

        return result
    return wrapper

@register_IVA
def calculate_IVA(product):
    return product.price * 0.13

my_product = Product(100)
calculate_IVA(my_product)