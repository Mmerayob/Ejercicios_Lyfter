# Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de funciones (exceptuando el 1 y 2).

from functions import sum_list, reverse_string, print_lower_upper_number_strings, print_phrase_sorted_alphabetically, validate_prime_numbers, create_new_list

def test_sum_list_empty_list_works():
    input_list = []
    result = sum_list(input_list)
    assert result == 0

def test_sum_list_decimal_numbers():
    input_list = [9.5,9.95]
    result = sum_list(input_list)
    assert result == 19.45


def test_sum_list_negative_numbers():
    input_list = [10,-9.50]
    result = sum_list(input_list)
    assert result == 0.5


def test_reverse_string_empty_string_works():
    input_string = ""
    new_string = reverse_string(input_string)
    assert new_string == ""


def test_reverse_string_large_phrase():
    input_string = "Las pruebas unitarias son funciones automatizadas que se integran en el código para verificar que partes individuales del mismo funcionen correctamente. Estas pruebas se enfocan en evaluar funciones específicas, asegurándose de que produzcan los resultados esperados con distintos conjuntos de entradas."
    new_string = reverse_string(input_string)
    assert new_string == input_string[::-1]


def test_reverse_string_multiple_characters():
    input_string = f"*Pruebas Unitarias: son funciones {100}% automatizadas"
    new_string = reverse_string(input_string)
    assert new_string == input_string[::-1]


def test_print_lower_upper_number_strings_empty_string(capsys):
    input_string = ""
    print_lower_upper_number_strings(input_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hay 0 letras mayúsculas y 0 letras minúsculas."


def test_print_lower_upper_number_strings_large_string(capsys):
    input_string = "Las pruebas unitarias son funciones automatizadas que se integran en el código para verificar que partes individuales del mismo funcionen correctamente. Estas pruebas se enfocan en evaluar funciones específicas, asegurándose de que produzcan los resultados esperados con distintos conjuntos de entradas."
    print_lower_upper_number_strings(input_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hay 2 letras mayúsculas y 258 letras minúsculas."


def test_print_lower_upper_number_strings_special_characters(capsys):
    input_string = "!#$%$%&/(()=)65410+-*"
    print_lower_upper_number_strings(input_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hay 0 letras mayúsculas y 0 letras minúsculas."


def test_print_phrase_sorted_alphabetically_normal():
    input_str = "python-variable-funcion-computadora-monitor"
    result = print_phrase_sorted_alphabetically(input_str)
    assert result == "computadora-funcion-monitor-python-variable"

def test_print_phrase_sorted_alphabetically_single_word():
    input_str = "python"
    result = print_phrase_sorted_alphabetically(input_str)
    assert result == "python"

def test_print_phrase_sorted_alphabetically_already_sorted():
    input_str = "arco-barrio-calle"
    result = print_phrase_sorted_alphabetically(input_str)
    assert result == "arco-barrio-calle"


def test_create_new_list_with_mixed_numbers():
    input_list = [1, 4, 6, 7, 13, 9, 67]
    result = create_new_list(input_list)
    assert result == [7, 13, 67]

def test_create_new_list_no_primes():
    input_list = [0, 1, 4, 6, 8, 9, 10]
    result = create_new_list(input_list)
    assert result == []

def test_create_new_list_empty_input():
    input_list = []
    result = create_new_list(input_list)
    assert result == []