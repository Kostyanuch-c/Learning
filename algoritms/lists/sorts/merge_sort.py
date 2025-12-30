def merge(first: list[int], second: list[int]) -> list[int]:
    first_index, second_index = 0, 0
    len_first, len_second = len(first), len(second)
    result = []
    while first_index < len_first and second_index < len_second:
        if first[first_index] <= second[second_index]:
            result.append(first[first_index])
            first_index += 1
        else:
            result.append(second[second_index])
            second_index += 1
    return result + first[first_index:] + second[second_index:]


def merged_sort_recursive(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2

    lst1 = merged_sort_recursive(arr[:middle_index])
    lst2 = merged_sort_recursive(arr[middle_index:])
    return merge(lst1, lst2)


def merged_sort_iterative(arr: list[int]) -> list[int]:
    # Разбиваем каждый элемент в отдельный список
    arr_1 = [[x] for x in arr]

    # Пока не осталось только один список
    while len(arr_1) > 1:
        new_arr = []
        i = 0
        while i < len(arr_1):
            if i + 1 < len(arr_1):
                # сливаем пары
                merged = merge(arr_1[i], arr_1[i + 1])
                new_arr.append(merged)
            else:
                # если не чётное количество — переносим последний как есть
                new_arr.append(arr_1[i])
            i += 2
        arr_1 = new_arr

    return arr_1[0]
if __name__ == '__main__':
    lst = [4, 2, 5, 1, 11, 3, 6, 3, 6789, 9, 7, 776, 521, 44, 32]
    print(merged_sort_iterative(lst))
