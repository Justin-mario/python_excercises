from decimal import Decimal


def college_exam():
    number_of_failure = 0
    number_of_pass = 0

    for number in range(10):
        grade = int(input("Enter grade: "))
        if grade == 1:
            number_of_failure += 1
        else:
            number_of_pass += 1
    print('number of failures ', number_of_failure)
    print('number of success ', number_of_pass)
    if number_of_pass >= 8:
        print("well done")
    else:
        print("need to seat up")


# college_exam()


def using_range():
    for i in range(10, 0, -1):
        print(i, end=" ")


# using_range()


def annual_interest_rate():
    annual_interest = Decimal('0.05')
    original_amount = Decimal('1000.00')

    print("Year", "\t\t\t\t\t\t\t\t\t\t", "amount on deposit")
    for i in range(1, 11):
        amount_on_deposit = original_amount * (1 + annual_interest) ** i
        print(f'year{i:<10} annual amount on deposit is {amount_on_deposit :>10.2}')


annual_interest_rate()
