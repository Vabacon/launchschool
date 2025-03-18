value = int(input("Enter a value between 5 and 9: "))

match value:
    case 5:
        print(f'Value is {value}.')
    case 6:
        print(f'Value is {value}.')
    case 7:
        print(f'Value is {value}.')
    case 8:
        print(f'Value is {value}.')
    case 9:
        print(f'Value is {value}.')
    case 1 | 2 | 3 | 4:
        print("Value is below 5.")
    case _:
        print("Not found.")

