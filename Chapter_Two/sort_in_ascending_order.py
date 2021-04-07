number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))

largest = middle = smallest = number1

if number2 > largest:
    largest = number2
if number3 > largest:
    largest = number3

if number2 < smallest:
    smallest = number2
if number3 < smallest:
    smallest = number3

if smallest < number1 < largest:
    middle = number1
if smallest < number2 < largest:
    middle = number2
if smallest < number3 < largest:
    middle = number3

print(largest, middle, smallest)
