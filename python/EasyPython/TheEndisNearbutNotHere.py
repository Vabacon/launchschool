# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.

# def penultimate(string):
#     string_list = string.split(' ')
#     return(string_list[-2])


def penultimate(string):
    return(string.split(' ')[-2])


# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
print(penultimate("Jumbo doggie want bye done!") == "bye")