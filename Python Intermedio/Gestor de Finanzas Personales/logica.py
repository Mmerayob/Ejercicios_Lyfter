from datetime import datetime

class Transaction:
    def __init__(self,date,name,amount,category,type):

        if type != "Ingreso" and type != "Gasto":
            raise ValueError("El tipo de transacción solo puede ser Ingreso o Gasto.")
            
        if amount <= 0:
            raise ValueError("El monto de la transacción debe ser positivo")

        self.date = date
        self.name = name
        self.amount = amount
        self.category = category
        self.type = type

class Category:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class FinanceManager:

    def __init__(self):
        self.transaction_list = []
        self.category_list = []

    def add_category(self, category):
        self.category_list.append(category)

    def has_categories(self):
        return len(self.category_list) > 0

    def add_transaction(self,transaction):
        self.transaction_list.append(transaction)

    def calculate_total_income(self):
        total_income = 0
        for transaction in self.transaction_list:
            if transaction.type == "Ingreso":
                total_income += transaction.amount
        return total_income

    def calculate_total_expense(self):
        total_expense = 0
        for transaction in self.transaction_list:
            if transaction.type == "Gasto":
                total_expense += transaction.amount
        return total_expense

    def calculate_overall_balance(self):
        return self.calculate_total_income() - self.calculate_total_expense()

    def filter_by_date_range(self, start_date_str, end_date_str):
        filtered_list = []        
        validated_start_date = datetime.strptime(start_date_str,"%d/%m/%Y").date()
        validated_end_date = datetime.strptime(end_date_str,"%d/%m/%Y").date()

        for transaction in self.transaction_list:
            validated_trans_date = datetime.strptime(transaction.date,"%d/%m/%Y").date()

            if validated_start_date <= validated_trans_date <= validated_end_date:
                filtered_list.append(transaction)
        return filtered_list
        
