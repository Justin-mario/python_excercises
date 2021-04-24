def square_root(number):
    return number**2


print(square_root(7))


def maximum_number(number1, number2, number3):
    max_value = number1
    if number2 > max_value:
        max_value = number2
    if number3 > max_value:
        max_value = number3
    return max_value


maximum_value = maximum_number(450, 67, -23)
print(maximum_value)
