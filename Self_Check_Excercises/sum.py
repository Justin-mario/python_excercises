
name = input("Enter Employee name: ")
hours_worked = eval(input("Enter Number of hours worked in a week: "))
pay_rate = eval(input("Enter hourly pay rate: "))

pay = hours_worked * pay_rate

federal_tax = eval(input("Enter tax withholding rate: "))
f_tax = pay * federal_tax/100

withholding_tax = eval(input("Enter withholding tax: "))
w_tax = pay * withholding_tax/100

total_pay = (pay - f_tax) - w_tax
print(f_tax, w_tax)
print("Weekly Pay After Tax is : ", format(total_pay, "5.2f"))
