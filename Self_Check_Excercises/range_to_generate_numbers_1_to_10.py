from decimal import Decimal
value = Decimal('2000.01')

for number in range(1, 11, 1):
    print(number, end=', ')

for set_of_numbers in range(1, 10, 1):
    print('\n', set_of_numbers, end=', ')

for counter in range(99, -11, -11):
    print(counter, end=", ")


total_sum = 0

for sum_of_number in range(2, 101, 2):
    total_sum += sum_of_number
print(f'{total_sum}')

