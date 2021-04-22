# finding 7% return on investment after 10, 20, 30 years.

principal = 1000.00
annual_rate_of_return = 0.07

for years in range(1, 31):
    return_on_investment = principal * (1 + annual_rate_of_return) ** years
    print("Years    ", f'{years:.2f}', "       Return On Investment       ", f'{return_on_investment:.2f}')
