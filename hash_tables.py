book = dict()
book["apple"] = .33
book["milk"] = 1.49
book["avocado"] = 1.49
print(book["avocado"])

def hash1(input):
    return 1

def hash_len_index(string):
    return len(string)

def hash_first_char(string):
    if string[0] == "a":
        return 0

def hash_prime(string):
    a = "a"
    b = "b"
    c = "c"
    d = 7
    c = 11
    g = "g"
    sum = 0
    for letter in string:
        if letter == "a":
            sum += 1
        elif letter == "b":
            sum += 13
        elif letter == "g":
            sum += 17
    return sum % 10
# print(hash1("sdsdsadc"))
#
# print(hash_len_index("sdsdsadc"))
#
# print(hash_first_char("asss"))

print(hash_prime("bag"))
