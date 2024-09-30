def binary_search_recursively(lst: list, val: int, left: int = 0, right: int = None) -> int:
    if right is None:
        right = len(lst) - 1

    middle = (left + right) // 2

    if left > right:
        return -1

    if lst[middle] == val:
        return middle

    if lst[middle] < val:
        return binary_search_recursively(lst=lst, val=val, left=middle + 1, right=right)

    return binary_search_recursively(lst=lst, val=val, left=left, right=middle - 1)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search_recursively(lst=lst, val=6))
