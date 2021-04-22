# palindrome
numbers = int(input("Input five numbers "))
first_int_division = numbers // 10000
first_modulo = numbers % 10000
second_int_division = first_modulo // 1000
second_modulo = first_modulo % 1000
third_int_division = second_modulo // 100
third_modulo = second_modulo % 100
fourth_int_division = third_modulo // 10
fourth_modulo = third_modulo % 10

print(first_int_division, " ", second_int_division, " ", third_int_division, " ", fourth_int_division, " ",
      fourth_modulo)

if first_int_division == fourth_modulo or second_int_division == fourth_int_division:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

counter = 1
count = 1
while count < 6:
    counter *= count
    count += 1


print(counter)

