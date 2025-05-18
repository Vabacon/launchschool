
def oddities(lst):
    oddlist = []
    for element in lst:
        if lst.index(element) == 0 or lst.index(element) % 2 == 0:
            oddlist.append(element)

    return(oddlist)




print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
