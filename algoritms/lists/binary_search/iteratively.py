def binary_search_iteratively(lst: list, val: int) -> int:
    left, right = 0, len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == val:
            return middle

        if lst[middle] < val:
            left = middle + 1
        else:
            right = middle - 1

    return -1


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search_iteratively(lst=lst, val=6))
