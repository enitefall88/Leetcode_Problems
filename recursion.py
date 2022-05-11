def inf_recursion(int):
    print(int)
    if int >= 10: # base case
        return # exit the execution
    else:
        inf_recursion(int + 1) #recursive case

inf_recursion(-33)
