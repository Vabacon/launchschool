number = int(input("Choose a number: "))

def number_in_range(number):
    if number >= 0 or number <= 50:
        print(f'Number {number} is between 0 and 50.')
    elif number >= 51 or number <= 100:
        print(f'Number{number} is between 51 and 100')
    elif number > 100:
        print(f'Number {number} is greater than 100.')
    elif number < 0:
        print(f'Number {number} is less than 0.')
    else:
        print("Idk what to tell you.")

number_in_range(number)
