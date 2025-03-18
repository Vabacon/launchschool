my_list = [[1, 3, 6, 11], [4, 2, 4], [9, 17, 16, 0]]

count = len(my_list)
index = 0
while index < count:
    subcount = len(my_list[index])
    subindex = 0
    while subindex < subcount:
        if my_list[index][subindex] % 2 == 0:
            print(my_list[index][subindex])
            subindex += 1
        else:
            subindex += 1
    index += 1
