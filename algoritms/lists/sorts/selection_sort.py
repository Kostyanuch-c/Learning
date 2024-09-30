def selection_sort(lst: list[int]) -> list[int]:
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


if __name__ == '__main__':
    lst = [2, 4, 5, 1, 5, 3, 6, 3, 6789, 9, 7, 776, 5, 44, 32]
    print(selection_sort(lst))
