def bubble_sort(list_to_sort):

    for outer_index in range(0,len(list_to_sort)-1):

        has_changed = False

        for index in range(0,len(list_to_sort)-1-outer_index):
            current_number = list_to_sort[index]
            next_number = list_to_sort[index+1]

            print(f"--Iteración {outer_index}, {index}. Número actual: {current_number}. Siguiente número: {next_number}")

            if current_number > next_number:
                print("Intercambiando el número mayor a la siguiente posición.")
                list_to_sort[index+1] = current_number
                list_to_sort[index] = next_number
                has_changed = True

        if not has_changed:
            return


list_to_sort = [1,2,3,6,5]
bubble_sort(list_to_sort)

print(list_to_sort)