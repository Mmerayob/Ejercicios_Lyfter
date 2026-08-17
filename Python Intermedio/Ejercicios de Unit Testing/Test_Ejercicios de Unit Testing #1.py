# 1. Cree los siguientes unit tests para el algoritmo bubble_sort:
#   Funciona con una lista pequeña.
#   Funciona con una lista grande (de más de 100 elementos.)
#   Funciona con una lista vacía.
#   No funciona con parámetros que no sean una lista.

import pytest
import random

from bubble_sort import bubble_sort

def test_bubble_sort_small_list_correctly():

    list_input = [5,3]

    bubble_sort(list_input)

    assert list_input == [3,5]


def test_bubble_sort_big_list_correctly():

    list_input = random.sample(range(-50,200),200)

    bubble_sort(list_input)

    assert list_input == sorted(list_input)


def test_bubble_sort_blank_list_works():

    list_input = []

    bubble_sort(list_input)

    assert list_input == []


def test_bubble_sort_with_incorrect_format_list():

    list_input = 8

    with pytest.raises(TypeError):
        bubble_sort(list_input)