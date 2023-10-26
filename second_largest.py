def second_largest(numbers):

    first_max = second_max = float('-inf')

    for num in numbers:
        if num > first_max:
            second_max = first_max
            first_max = num
            print(first_max,second_max)
        elif num > second_max and num != first_max:

            second_max = num

    if second_max == float('-inf'):
        return "No second largest element found"

    return second_max


# Example usage
numbers = [1, 3, 4, 2, 121, 4, 54]
result = second_largest(numbers)
#print("Second largest number is:", result)


def largest(list):
    max_num = second_max_num = float('-inf')
    for num in list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
    print(second_max_num)
largest([1, 3, 4, 2, 121, 4, 54])
