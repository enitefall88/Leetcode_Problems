def phoneNumbers(array):
    result = []
    print(array)
    print(result)
    if array == []:
        return result
    else:
        return phoneNumbers(array[1:]) # slicing from the start


print(phoneNumbers(array=[0,1,2,3,4,5,6]))
