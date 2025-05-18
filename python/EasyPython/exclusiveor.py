
def xor(arg_a, arg_b):
    if arg_a and arg_b:
        return(False)
    elif arg_a == False and arg_b == False:
        return(False)
    else:
        return(True)




print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
print(xor(False, False) == False)