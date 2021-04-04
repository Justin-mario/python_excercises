
number1 = int(input('Enter First Number  '))
number2 = int(input('Enter Second Number  '))
number3 = int(input('Enter third number  '))

minimum_value = number1
maximum_value = minimum_value

if number2 < minimum_value:
    minimum_value = number2
else:
    maximum_value = number2
if number3 < minimum_value:
    minimum_value = number3
else:
    maximum_value = number3

print('Minimum value is: ', minimum_value, 'Maximum value is: ', maximum_value)
