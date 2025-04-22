# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def absolute(number):
    return('False' if abs(number) % 2 != 0 else 'True')

print(absolute(1))
print(absolute(-10))
print(absolute(4))
print(absolute(-41))