import FreeSimpleGUI as sg
from logica import Transaction, Category, FinanceManager
from persistencia import save_data, load_data, export_csv_data
from datetime import date, datetime

manager = FinanceManager()
load_data(manager)

def get_table_data(manager, custom_list=None):
    transactions = (
        custom_list if custom_list is not None else manager.transaction_list
    )
    return [
        [t.date, t.name, f"${t.amount}", t.category.name, t.type]
        for t in transactions
    ]

def get_row_colors(manager, custom_list=None):
    transactions = (
        custom_list if custom_list is not None else manager.transaction_list
    )
    return [
        (index, "black", t.category.color)
        for index, t in enumerate(transactions)
    ]

def parse_amount(amount_string):

    amount_validated = float(amount_string)

    if amount_validated <= 0:
        raise ValueError("El monto deber ser positivo")
    return amount_validated


def validate_isnot_future_date(selected_date):

    parse_date = datetime.strptime(selected_date, "%d/%m/%Y").date()
    return parse_date <= date.today()

def validate_required_fields(selected_date,selected_title,selected_amount,selected_category):

    if(not selected_date
        or not selected_title
        or not selected_amount
        or not selected_category 
    ):
        return False
    return True

def process_transaction_form(values,manager,transaction_type):

    date_values = values["-DATE-"]
    title_values = values["-TITLE-"]
    amount_values = values["-AMOUNT-"]
    category_values = values["-CATEGORY-"]

    # Validate all fields were filled
    if not validate_required_fields(date_values,title_values,amount_values,category_values):
        sg.popup_error("Debe llenar todos los campos obligatorios.")
        return False

    # Validate date is not in the future
    if not validate_isnot_future_date(date_values):
        sg.popup_error("No se pueden registrar movimientos con fecha futura.")
        return False

    # Validate amount format
    try:
        amount_validated = parse_amount(amount_values)
    except ValueError:
        sg.popup_error("El monto debe ser un número válido y mayor a cero.")
        return False

    category_obj = next(c for c in manager.category_list if c.name == category_values)

    new_trans = Transaction(
        date=date_values,
        name=title_values,
        amount=amount_validated,
        category=category_obj,
        transaction_type=transaction_type
        )

    manager.add_transaction(new_trans)
    save_data(manager)

    return True

def get_category_names(manager):

    if not manager.has_categories():
        sg.popup_error(
            "Debe crear al menos una categoría antes de registrar un movimiento."
        )
        return None
    return [cat.name for cat in manager.category_list]



headings=["Fecha", "Título", "Monto", "Categoría", "Tipo"]

layout = [
    [sg.Text("Gestor de Finanzas Personales")],
    [sg.Button("Añadir Ingreso",expand_x=True), sg.Button("Añadir Gasto",expand_x=True), sg.Button("Categoría",expand_x=True)],
    [
    sg.Text("Fecha Inicio:"), sg.Input(key="-START_DATE-",size=(10,1),disabled=True),
    sg.CalendarButton("Seleccionar Fecha",target="-START_DATE-",format="%d/%m/%Y"),
    sg.Text("Fecha Fin:"), sg.Input(key="-END_DATE-",size=(10,1),disabled=True),
    sg.CalendarButton("Seleccionar Fecha",target="-END_DATE-",format="%d/%m/%Y"),
    sg.Button("Filtrar",expand_x=True),sg.Button("Limpiar Filtro"),
    ],
    [sg.Table(values= get_table_data(manager),
            headings=headings,
            auto_size_columns=True,
            num_rows=10,
            row_colors=get_row_colors(manager),
            expand_x = True,
            expand_y = True,
            key="-TABLE-")
            ],
    [sg.Button("Exportar CSV")],
]

def make_layout_transaction(title_text, category_list):
    return [
        [sg.Text(title_text)],
        [
            sg.Text("Fecha:"), 
            sg.Input(key="-DATE-", size=(15, 1), disabled=True, default_text=date.today().strftime("%d/%m/%Y")),
            sg.CalendarButton("Seleccionar Fecha", target="-DATE-", format="%d/%m/%Y")
        ],
        [sg.Text("Título:"), sg.Input(key="-TITLE-", size=(35, 1))],
        [sg.Text("Monto:"), sg.Input(key="-AMOUNT-", size=(15, 1))],
        [sg.Text("Categoría:"), sg.Combo(values=category_list, key="-CATEGORY-", readonly=True)],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]

def make_layout_category():
    return [
        [sg.Text("Nombre:"),sg.Input(key="-NAME-",size=(35,1))],
        [sg.Text("Color de Categoría:"),sg.Input(key="-COLOR-",size=(15,1)),sg.ColorChooserButton("Elegir Color",target=("-COLOR-"))],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]


window = sg.Window("Gestor de Finanzas Personales", layout,resizable=True)

while True:

    event_main, values_main = window.read()
    
    if event_main == sg.WIN_CLOSED:
        break

    # Filter dates Event
    if event_main == "Filtrar":
        start_date = values_main["-START_DATE-"]
        end_date = values_main["-END_DATE-"]

        if not start_date or not end_date:
            sg.popup_error("Debe seleccionar ambas fechas para aplicar el filtro.")
        else:
            filtered_list = manager.filter_by_date_range(start_date, end_date)

            if not filtered_list:
                sg.popup_info("No se encontraron transacciones en el rango seleccionado.")

            window["-TABLE-"].update(
                values=get_table_data(manager, filtered_list),
                row_colors=get_row_colors(manager, filtered_list)
            )

    # Clear the Filter dates Event
    if event_main == "Limpiar Filtro":
        window["-START_DATE-"].update("")
        window["-END_DATE-"].update("")
        window["-TABLE-"].update(
            values=get_table_data(manager), row_colors=get_row_colors(manager)
        )

# Income Window:
    if event_main == "Añadir Ingreso":
        category_names = get_category_names(manager)
        if category_names is not None:
            window_income = sg.Window(
                "Añadir Ingresos", make_layout_transaction("Añadir Nuevo Ingreso",category_names)
            )

            while True:
                event_income, values_income = window_income.read()

                if event_income == "Guardar":
                    if process_transaction_form(values_income, manager, "Ingreso"):
                        window["-TABLE-"].update(values=get_table_data(manager))
                        window["-TABLE-"].update(row_colors=get_row_colors(manager))
                        break

                if event_income in (sg.WIN_CLOSED, "Cancelar"):
                    break

            window_income.close()

    # Expense Window:
    if event_main == "Añadir Gasto":
        category_names = get_category_names(manager)
        if category_names is not None:
            window_expense = sg.Window(
                "Añadir Gastos", make_layout_transaction("Añadir Nuevo Gasto",category_names))

            while True:
                event_expense, values_expense = window_expense.read()

                if event_expense == "Guardar":
                    if process_transaction_form(values_expense, manager, "Gasto"):
                        window["-TABLE-"].update(values=get_table_data(manager))
                        window["-TABLE-"].update(row_colors=get_row_colors(manager))
                        break

                if event_expense in (sg.WIN_CLOSED, "Cancelar"):
                    break

            window_expense.close()


    # Category Window:

    if event_main == "Categoría":
            window_category = sg.Window("Categoría", make_layout_category())
    
            while True:
                event_category, values_category = window_category.read()
                    
                if event_category == "Guardar":

                    #Validate empty fields
                    if not values_category["-NAME-"] or not values_category["-COLOR-"]:
                        sg.popup_error("Por favor ingresa un nombre y selecciona un color.")
                        continue

                    try:
                        new_cat = Category(
                            name=values_category["-NAME-"], color=values_category["-COLOR-"]
                            )
                        manager.add_category(new_cat)
                        save_data(manager)
                        break

                    except ValueError as error:
                        sg.popup_error(str(error))
                        continue

                if event_category in (sg.WIN_CLOSED,"Cancelar"):
                    break

            window_category.close()

    # Export CSV Window

    if event_main == "Exportar CSV":
        if not manager.transaction_list:
            sg.popup_error("No hay transacciones registradas para exportar.")
        else:
            csv_saved, message = export_csv_data(manager)
            if csv_saved:
                sg.popup(message,title="Éxito")
            else:
                sg.popup_error(message,title="Error al Exportar")

window.close()


