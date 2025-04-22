# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# (print(number) for number in range(1, 100) if number % 2 != 0)

# for number in range(1, 100):
#     print(number if number % 2 != 0 else number)
    # you can modify the else statement to print something else or nothing.

even_numbers = []
for number in range(1, 100):
    if number % 2 == 0:
        even_numbers.append(number)

for _ in even_numbers:
    print(_)