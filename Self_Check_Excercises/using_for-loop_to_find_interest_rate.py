years = 1
rate = 0.05
principal = 1000.00

for years in range(1, 11):
    amount = principal*((1 + rate) ** years)
    print(f'{years: > 2}{amount: > 10.2f}')


