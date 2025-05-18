
def negative(num):
    return((num * (-1) if num > 0 else num))


print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True