# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product
# of all numbers between 1 and the entered integer, inclusive.

# input > 0
# output is the sum or product of all int between input and 1.
#

number = int(input('Select a number greater than zero: '))
sop = input('["s" for Sum or "p" for Product]: ')
total = 0
if sop == 's':
    for num in range(1, number + 1):
        total += num
if sop == 'p':
    total += 1
    for num in range(1, number + 1):
        total *= num

print(total)