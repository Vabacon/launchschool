
max = '0'
for number in ['10', '2', '35', '6', '25']:
    if int(number) > int(max):
        print(number)
        max = number
    else:
        print('Still looking...')

print('Max value is:', max)