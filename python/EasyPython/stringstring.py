
def stringy(integer):
    binary_list = ['1']
    for _ in range(integer - 1):
        binary_list.append('0') if binary_list[-1] == '1' else binary_list.append('1')
    return(''.join(binary_list))



print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True