def binary_search(array_list, target):
    left = 0
    right = len(array_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if array_list[mid] < target:
            left = mid + 1
        elif array_list[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

print(binary_search(array_list=[1,3,4,5,6,7,8,9], target=9))
