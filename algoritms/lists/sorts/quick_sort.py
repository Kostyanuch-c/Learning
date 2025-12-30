def quick_sort(arr: list[int]) -> list[int]:
    # Сохраняем длину массива в переменную.
    len_array = len(arr)

    # Базовый случай рекурсии. Если длина массива меньше или равна 1,
    # то возвращаем этот массив, тем самым запуская обратный ход рекурсии.
    if len_array <= 1:
        return arr
    # Определяем индекс опорного элемента и получаем сам опорный элемент:
    middle_element_index = len_array // 2
    pivot = arr[middle_element_index]  # pivot - "ось, точка опоры".
    # Делим массив на три части: left, center и right.
    left, center, right = [], [], []
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            center.append(element)
 
    return quick_sort(left) + center + quick_sort(right)
    # Для каждой части массива рекурсивно вызываем функцию quicksort().


if __name__ == '__main__':
    lst = [4, 2, 5, 1, 11, 3, 6, 3, 6789, 9, 7, 776, 521, 44, 32]
    print(quick_sort(lst))
