# def factorial(num):
#     product = 1
#     while num > 1:
#         product *= num
#         num -=1
#     return product


def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number
    return result


print(factorial(6))