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
