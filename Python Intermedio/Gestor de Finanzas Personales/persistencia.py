import json
import csv

from logica import Transaction, Category


def category_to_dict(categ):
    return {"name": categ.name, "color": categ.color}


def transaction_to_dict(transac):
    return {"date": transac.date, "name": transac.name, "amount": transac.amount, 
        "category": category_to_dict(transac.category), "type": transac.type}


def save_data(manager, filename="data.json"):
    
    categories_list = [category_to_dict(cat) for cat in manager.category_list]

    transactions_list = [transaction_to_dict(trans) for trans in manager.transaction_list]

    data = {"categories": categories_list, "transactions": transactions_list}

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def dict_to_category(data):

    return Category(data["name"],data["color"])


def dict_to_transaction(data):

    return Transaction(data["date"],data["name"],data["amount"],dict_to_category(data["category"]),data["type"])


def load_data(manager, filename="data.json"):

    try:
        with open(filename,"r") as f:
            data = json.load(f)

        manager.category_list = [dict_to_category(cat) for cat in data.get("categories", [])]
        manager.transaction_list = [dict_to_transaction(trans) for trans in data.get("transactions",[])]

    except FileNotFoundError:
        pass

def export_csv_data(file_path, manager):

    headers = ["Fecha","Título","Monto","Categoría","Tipo"]

    try:

        with open(file_path,'w',encoding='utf-8-sig',newline='') as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            for trans in manager.transaction_list:
                writer.writerow({
                    "Fecha": trans.date,
                    "Título": trans.name,
                    "Monto": trans.amount,
                    "Categoría": trans.category.name,
                    "Tipo": trans.type,
                })
            
            file.write("\n")
            file.write("Totales:\n")
            file.write(f"Total de ingresos: ₡{manager.calculate_total_income():.0f}\n")
            file.write(f"Gastos: ₡{manager.calculate_total_expense():.0f}\n")
            file.write(f"Balance Neto: ₡{manager.calculate_overall_balance():.0f}\n")

        return True

    except Exception as e:
        return False