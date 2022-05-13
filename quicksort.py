def sum_up(array):
    result = 0
    for element in array:
        result += element
    print(result)

#sum_up(array=[2,3,4,5])

def sum_up_recursively(array):
  if array == []:
      return 0
  else:
       return array[0] + sum_up_recursively(array[1:]) #slices off from the first element

# return 2 + sum_up_recursively([3,4,5])
# return 3  sum_up_recursively([4,5])
# return 4 sum_up_recursively(5)  - stack top? and goes from here - 4 + 5 = 9
#  9 + 3 = 12
# 12 + 2 = 14
#print(sum_up_recursively(array=[2,3,4,5]))

# def pop_array(array):
#     result = []
#     i = 0
#     while i < len(array): # if array is empty then 0 < 0 is not true and stops running
#         result.append(array.pop(i))
#         print(array)
#
#     return result
#
# print(pop_array([2,3,4,5]))

def sum_up_recursively_with_pop(array): # this does not work
  if array == []:
      return 0
  else:
      return array[0] + sum_up_recursively_with_pop(array.remove(array[0])) # does not work because returns the first el?

#  sum_up_recursively_with_pop(array=[2,3,4,5])

#recursive function to count items in a list
def count_list_items(list):
    if list == []: # does not exit here because of the call stack is full?
       return 0
    else:
        return 1 + count_list_items(list[1:])  # every run is +1

count_list_items([2,3,4,5]) # how can we return and use the final result in a recursive function?

#recursive maximum number in a list
def maximum_number(list):
    if len(list) == 2:
        return list[0] if list[1] > list[0] else list[1]
        submax = maximum_number(list[1:]) # iterating through all elements of the list
        return list[0] if list[0] > submax else submax #

maximum_number([2,3,4,5])


def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

max([2,3,4,5])
