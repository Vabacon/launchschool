
def crunch(string):
    if string == '':
        return(string)

    string_list = list(string)
    crunched_list = [string_list[0]]
    char_index = 1

    for char in string_list:
        if char != crunched_list[-1]:
            crunched_list.append(char)
            char_index += 1
    return(''.join(crunched_list))


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')