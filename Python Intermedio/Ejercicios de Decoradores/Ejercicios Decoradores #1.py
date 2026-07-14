# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

class Product:
    def __init__(self,price):
        self.price = price

def register_IVA(func):
    def wrapper(*args, **kwargs):

        print(f"Parámetros recibidos posicionales (*args): {args}")
        print(f"Parámetros recibidos por nombre (**kwargs): {kwargs}")
            
        result = func(*args, **kwargs)

        print(f"Valor de retorno de la función: {result}")

        return result
    return wrapper

@register_IVA
def calculate_IVA(product, iva_rate = 0.13):
    return product.price * iva_rate

my_product = Product(150)
calculate_IVA(my_product)
calculate_IVA(my_product, iva_rate = 0.15)