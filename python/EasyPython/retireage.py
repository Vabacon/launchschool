# Build a program that displays when the user will retire and
# how many years she has to work till retirement.

age = input('What is your age? ')
std_retierment_age = 64
current_year = 2025

if int(age) > std_retierment_age:
    print("You're already retired! YAY!")
else:
    years_left = std_retierment_age - int(age)
    retirement_year = current_year + years_left
    print(f'You will retire in {retirement_year}')
    print(f'You have {years_left} years to go!')