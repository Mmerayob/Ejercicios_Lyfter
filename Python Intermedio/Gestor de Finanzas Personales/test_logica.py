import pytest

from logica import Transaction, FinanceManager, Category

@pytest.fixture
def manager():
    return FinanceManager()

def test_create_category():
    category = Category("Salario","#FF5733")
    assert category.name == "Salario"
    assert category.color == "#FF5733"

def test_create_transaction_incorrect_type():
    category = Category("Salario","#FF5733")
    with pytest.raises(ValueError):
        Transaction("01/08/2026","Salario Mensual",2000,category,"Otro")

def test_create_transaction_negative_amount():
    category = Category("Salario","#FF5733")
    with pytest.raises(ValueError):
        Transaction("01/08/2026","Salario Mensual",-1,category,"Ingreso")

def test_has_categories(manager):

    category = Category("Salario","#FF5733")
    manager.add_category(category)
    assert manager.has_categories() is True

def test_has_categories_cuando_esta_vacia(manager):
    assert manager.has_categories() is False

def test_calculate_total_income(manager):

    category = Category("Salario","#FF5733")
    transaction_1 = Transaction("01/08/2026","Salario Mensual",2000,category,"Ingreso")
    transaction_2 = Transaction("01/08/2026","Salario Mensual",1000,category,"Ingreso")

    manager.add_transaction(transaction_1)
    manager.add_transaction(transaction_2)

    assert manager.calculate_total_income() == 3000


def test_calculate_total_expense(manager):

    category = Category("Comida","#FF5733")
    transaction_1 = Transaction("01/08/2026","Cena",2000,category,"Gasto")
    transaction_2 = Transaction("01/08/2026","Almuerzo",1000,category,"Gasto")

    manager.add_transaction(transaction_1)
    manager.add_transaction(transaction_2)

    assert manager.calculate_total_expense() == 3000


def test_calculate_overall_balance(manager):
    category_ingreso = Category("Salario", "#00FF00")
    category_expense = Category("Comida", "#FF0000")

    income = Transaction("01/08/2026", "Nomina", 2000, category_ingreso, "Ingreso")
    expense = Transaction("31/08/2026", "Almuerzo", 500, category_expense, "Gasto")

    manager.add_transaction(income)
    manager.add_transaction(expense)

    assert manager.calculate_overall_balance() == 1500