# def findSmallest(arr):
#     # Stores the smallest value
#     smallest = arr[0]
#     # Stores the index of the smallest value
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest_index = i
#             smallest = arr[i]
#     return smallest
#
#
# print(findSmallest(arr=[4, 5, 6, 7, 3, 1]))
#
#
# def selectionSort(arr):
#     resultArray = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         resultArray.append(arr.pop(smallest))
#     return resultArray
#
#
# print(selectionSort([4, 5, 6, 7, 3]))
#



# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]
  return smallest_index

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest)) # removing smallest and adding it to the result array
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))
