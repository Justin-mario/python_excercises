# program to find factorial
counter = 1
factorials = 1
number = int(input(" input a number to find the factorial "))
while counter < number:
    factorials *= counter
    counter += 1
print(factorials)
