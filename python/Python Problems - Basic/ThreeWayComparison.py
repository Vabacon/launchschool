def compare_by_length(str1, str2):
    if len(str1) == len(str2):
        return(0)
    return(1 if len(str1) > len(str2) else -1)



print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity') )     #  1
print(compare_by_length('humor', 'grace') )          #  0