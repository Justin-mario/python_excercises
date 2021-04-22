# program to find sum, average, product, minimum and maximum number
total_sum = 0
product = 0
average = 0
maximum_value = 0
minimum_value = 0
list_of_number = []
count = 1
while count < 4:
    number = int(input('Enter First Number  '))
    list_of_number.append(number)
    product *= number
    total_sum = sum(list_of_number)
    average = (total_sum / len(list_of_number))
    maximum_value = max(list_of_number)
    minimum_value = min(list_of_number)
    count += 1
print("Sum is: ", total_sum, "\nAverage is: ", average, "\nProduct is: ", product)
print("Largest Number is:\t", maximum_value, "\nSmallest Number is:\t", minimum_value)
