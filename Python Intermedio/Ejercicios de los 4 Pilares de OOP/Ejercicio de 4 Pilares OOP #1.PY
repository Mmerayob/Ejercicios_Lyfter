# Cree una clase de BankAccount que:
# 1. Tenga un atributo de balance.
# 2. Tenga un método para ingresar dinero.
# 3. Tenga un método para retirar dinero.
# 
# Cree otra clase que herede de esta llamada SavingsAccount que:
# 1. Tenga un atributo de min_balance que se pueda asignar al crearla.
# 2. Arroje un error si al intentar retirar dinero, el retiro haría que 
#    el balance quede debajo del min_balance. Es decir que sí se pueden 
#    hacer retiros siempre y cuando el balance quede arriba del min_balance.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit_money(self,money):
        self.balance += money
        return self.balance
    
    def withdraw_money (self,money):
        self.balance -= money
        return self.balance

class SavingsAccount (BankAccount):
    def __init__(self, min_balance,initial_balance=0):
        super().__init__(initial_balance)
        self.min_balance = min_balance

    def withdraw_money (self,money):
        
        if self.min_balance > self.balance - money:
            raise ValueError(f"Error: No puede retirar el dinero solicitado porque sobrepasa el minimo en su cuenta de {self.min_balance}")
        else:
            return super().withdraw_money(money)