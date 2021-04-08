# finding odd and even number

for count in range(4, 10):
    value = int(input("input number: "))
    if value % 2 == 1:
        print(f"{value} odd number")
    if value % 2 == 0:
        print(value, "even number")
