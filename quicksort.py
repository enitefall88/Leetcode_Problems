def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()


    items_greater = []
    items_lower = []
    for item in list:
        if item > pivot:
           items_greater.append(item)
        else:
             items_lower.append(item)
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

print(quicksort([1,2,3,4,3,3,4,5,6,7]))


def quicksort2(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
    items_greater = []
    items_smaller = []
    for i in list:
        if list[i] < pivot:
            items_smaller.append(i)
        else:
            items_greater.append(i)
    return quicksort(items_smaller) + [pivot] + quicksort(items_greater)

print(quicksort2([1,2,3,4,3,3,4,5,6,7]))
