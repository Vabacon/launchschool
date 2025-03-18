numbers = range(1, 10 + 1)

# def even_or_odd(num):
#     for number in num:
#         if number % 2 == 0:
#             print(f'Number {number} is even!')
#         else:
#             print(f'Number {number} is odd!')

# even_or_odd(numbers)

def even_or_odd(num):
    for number in num:
        print("Even" if number % 2 == 0 else "Odd")
even_or_odd(numbers)


