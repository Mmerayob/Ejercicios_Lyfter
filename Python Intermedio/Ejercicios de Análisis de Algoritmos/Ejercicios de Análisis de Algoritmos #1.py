# Analice el algoritmo de bubble_sort usando la Big O Notation.

def bubble_sort(list_to_sort):

    for outer_index in range(0,len(list_to_sort)-1): # O(n)

        has_changed = False # O(1)

        for index in range(0,len(list_to_sort)-1-outer_index): # O(n^2)
            current_number = list_to_sort[index]  # O(1)
            next_number = list_to_sort[index+1]   # O(1)

            print(f"--Iteración {outer_index}, {index}. Número actual: {current_number}. Siguiente número: {next_number}") # O(1)

            if current_number > next_number: # O(1)
                print("Intercambiando el número mayor a la siguiente posición.") # O(1)
                list_to_sort[index+1] = current_number # O(1)
                list_to_sort[index] = next_number # O(1)
                has_changed = True  # O(1)

        if not has_changed: # O(1)
            return  # O(1)