def buble_sort(lst: list[int]) -> list[int]:
    for j in range(len(lst)):
        for i in range(len(lst) - 1 - j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


if __name__ == '__main__':
    lst = [2, 4, 5, 1, 5, 3, 6, 3, 6789, 9, 7, 776, 5, 44, 32, ]
    print(buble_sort(lst))
