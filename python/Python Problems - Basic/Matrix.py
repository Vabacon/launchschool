
sub_list = ["-", "-", "-"]
matrix = []

for i in range(3):
    matrix.append(sub_list.copy())

print(matrix)

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
