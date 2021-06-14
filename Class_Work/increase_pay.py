
pay = 300

score = eval(input("Enter pay "))

if score > 90:
    pay = (pay * 0.03) + pay
    print(pay)
else:
    pay = (pay * 0.01) + pay
    print(pay)