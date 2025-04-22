# Create a simple tip calculator.
# The program should prompt for a bill amount and a tip rate.
# The program must compute the tip,# then print both the tip and the total amount of the bill.
# You can ignore input validation and assume that the user will enter valid numbers.

bill_amt = int(input('Total bill amount: '))
tip_rate = int(input('Tip % rate: '))

tip_amt = bill_amt / tip_rate


print(f'Bill total is {bill_amt}.')
print(f'Tip total is {tip_amt}')