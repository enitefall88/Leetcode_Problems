def binary_search(array_list, target):
    left = 0
    right = len(array_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if array_list[mid] < target:  # determining
            left = mid + 1  # here is cutting the array in two from the left
        elif array_list[mid] > target:
            right = mid - 1  # cutting the array from the right
        else:
            return mid  # loop until the index of the target is found
    return -1


print(binary_search(array_list=[1, 3, 5, 6, 7, 8, 9, 11, 55, 89, 999], target=0))
