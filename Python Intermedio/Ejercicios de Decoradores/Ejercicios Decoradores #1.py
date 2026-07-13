# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

class Product:
    def __init__(self,price):
        self.price = price

def register_IVA(func):
    def wrapper(*args, **kwargs):
            
        result = func(*args, **kwargs)

        return result
    return wrapper

@register_IVA
def calculate_IVA(product):
    print(product.price * 0.13)

my_product = Product(150)
calculate_IVA(my_product)