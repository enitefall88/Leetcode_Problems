def phoneNumbers(array):
    result = []
    if array == []:
        return result
    else:
        result.append(phoneNumbers(array[1:]))

print(phoneNumbers())
