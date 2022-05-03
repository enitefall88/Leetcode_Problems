# def binarySearch(numbers, target):
#     left = 0  # index
#     right = len(numbers - 1)  # index
#
#     while left <= right:
#         mid = (left + right) / 2  # middle index position
#         if numbers[mid] > target:
#             left = mid + 1
#         elif numbers[mid] < target:
#             right = mid - 1
#         else:
#             return mid
#     return -1
#
#
# binarySearch([-3, 4, 5, 6, 8, 9, 12, 16], 9)


def search_iterative(arraylist, item):
    # low and high keep track of which part of the list you'll search in.
    low = 0
    high = len(arraylist) - 1

    # While you haven't narrowed it down to one element ...
    while low <= high:
        # ... check the middle element
        mid = (low + high) // 2
        guess = arraylist[mid]
        # Found the item.
        if guess == item:
            return mid
        # The guess was too high.
        if guess > item:
            high = mid - 1
        # The guess was too low.
        else:
            low = mid + 1

    # Item doesn't exist
    return None


letsdo = search_iterative(arraylist = [-3, 4, 5, 6, 8, 9, 12, 16], item = 9)
print(letsdo)
