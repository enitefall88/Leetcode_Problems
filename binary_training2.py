# Given an array of integers nums which is sorted in ascending order,
# and an integer target,
# write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# def binary_search(arr, target):

def binary_search(given_list, target):
    left = 0
    right = len(given_list) - 1
    while left <= right:
        middle_index = (left + right) //2
        if target > given_list[middle_index]:
            left += 1
        elif target < given_list[middle_index]:
            right -= 1
        else:
            return given_list[middle_index]
    return -1


print(binary_search([1,3,4,5,6,7,8,9], target=9))
