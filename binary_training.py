# def binary_search(array_list, target):
#     left = 0
#     right = len(array_list) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array_list[mid] < target:
#             left = mid + 1
#         elif array_list[mid] > target:
#             right = mid - 1
#         else:
#             return mid
#     return -1
#
# print(binary_search(array_list=[1,3,4,5,6,7,8,9], target=9))


# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
def binary_search(arr, target):
   left = 0
   right = len(arr) - 1

   while left <= right:
       mid = (right + left) // 2
       #id = (right - left)//2 # with every iteration calculate the middle, //2 rounds down
       if arr[mid] < target:
           left = mid + 1
       elif arr[mid] > target:
           right = mid - 1
       else:
           return mid
   return -1

print(binary_search(arr=[1,3,4,5,6,7,8,9], target=9))

#print(binary_search(arr=[1,3,4,6,8,11], target=11))
