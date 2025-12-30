def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        cur = arr[i]
        prev_index = i - 1
        while prev_index >= 0 and arr[prev_index] > cur:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1

        arr[prev_index + 1] = cur

    return arr


if __name__ == '__main__':
    lst = [4, 2, 5, 1, 5, 3, 6, 3, 6789, 9, 7, 776, 5, 44, 32]
    print(insertion_sort(lst))
