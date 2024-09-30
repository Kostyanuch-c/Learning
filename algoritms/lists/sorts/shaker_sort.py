def shaker_sort(lst: list[int]) -> list[int]:
    for j in range(len(lst)):
        flag = None
        for i in range(len(lst) - 1 - j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True

        for i in range(len(lst) - 2 - j, j, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                flag = True

        if not flag:
            break
    return lst

#
# def shaker_sort(lst: list[int]) -> list[int]:
#     left = 0
#     right = len(lst) - 1
#
#     while left <= right:
#         flag = False
#
#         # Проход слева направо
#         for i in range(left, right):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 flag = True
#
#         right -= 1  # Уменьшаем правую границу
#
#         # Проход справа налево
#         for i in range(right, left, -1):
#             if lst[i] < lst[i - 1]:
#                 lst[i], lst[i - 1] = lst[i - 1], lst[i]
#                 flag = True
#
#         left += 1  # Увеличиваем левую границу
#
#         if not flag:  # Если перестановок не было, список отсортирован
#             break
#
#     return lst

if __name__ == '__main__':
    lst = [2, 4, 5, 1, 5, 3, 6, 3, 6789, 9, 7, 776, 5, 44, 32, ]
    print(shaker_sort(lst))
