from decimal import Decimal
years = 1
rate = Decimal(0.05)
principal = Decimal('1000.00')
count = 1
while years < 11:
    amount = principal * ((1 + rate) ** years)
    print(f'{years: > 2}{amount: > 10.2f}')
    years += 1

