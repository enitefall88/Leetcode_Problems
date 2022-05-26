# def find_smallest_element(array):
#     smallest = array[0]
#     smallest_index = 0
#     for i in range(1, len(array)):
#         if array[i] < smallest:
#             smallest = array[i]
#             smallest_index = i # just index
#     return smallest_index
#
#
# def selection_sort(array):
#     resulting_array = []
#     for i in range(len(array)): # returns a sequence of int starting from 0
#         print(len(array),i) # len(array) to gp from i=0 to i=4 to reach the end of array
#         smallest = find_smallest_element(array) # returns index as an int
#         resulting_array.append(array.pop(smallest))
#     return resulting_array
#
# print(selection_sort(array=[4,3,5,6,7]))


def find_smallest_el_index(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    result = []
    for i in range (0, len(array)):
        smallest = find_smallest_el_index(array)
        result.append(array.pop(smallest))
    return result

print(selection_sort([4,3,5,6,7,1]))
