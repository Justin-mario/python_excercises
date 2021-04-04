# Finding
number1 = int(input('Enter First Number  '))
number2 = int(input('Enter Second Number  '))
number3 = int(input('Enter third number  '))

total_sum = (number1 + number2 + number3)
average = (total_sum/3)
product = (number1 * number2 * number3)

maximum_value = max(number1, number2, number3)
minimum_value = min(number1, number2, number3)

print("Sum is: ", total_sum, "\nAverage is: ", average, "\nProduct is: ", product)
print("Largest Number is:\t", maximum_value, "\nSmallest Number is:\t", minimum_value)
