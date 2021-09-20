class Account:

    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance


    def get_balance(self):
        return self.balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance and self.balance > 0:
            self.balance -= amount



