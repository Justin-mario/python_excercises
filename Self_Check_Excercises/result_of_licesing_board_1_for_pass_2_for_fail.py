
counter = 0
passed = 0
failed = 0

while counter < 10:
    grade = int(input("Enter result: "))
    if grade == 1:
        passed += 1
    else:
        failed += 1
    counter += 1
print("Number of Pass: ", passed, "\nNumber of Failed: ", failed)
if passed >= 8:
    print("Bonus to instructor!")
