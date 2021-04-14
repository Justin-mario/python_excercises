from decimal import Decimal


def resturant_bill_calculator():
    tax_rate = Decimal('0.0625')
    bill = Decimal('37.45')
    total_bill = Decimal((tax_rate * bill) + bill)
    return total_bill


print(f"{'Total Bill Is: '}{resturant_bill_calculator():.2f}")
