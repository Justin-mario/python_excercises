import unittest
from account.account import Account


class AccountTest(unittest.TestCase):
    def test_balance(self):
        account = Account('ken uzo', 1, 0.0)
        balance = account.get_balance()
        self.assertEqual(True, balance == 0)

    def test_deposit(self):
        account = Account('ken uzo', 1, 0.0)
        balance = account.get_balance()
        self.assertEqual(True, balance == 0)
        account.deposit(2000)
        balance = account.get_balance()
        assert balance == 2000

    def test_no_negative_deposit(self):
        account = Account('ken uzo', 1, 0.0)
        balance = account.get_balance()
        self.assertEqual(True, balance == 0)
        account.deposit(-2000)
        balance = account.get_balance()
        assert balance == 0


    def test_withdraw(self):
        account = Account('ken uzo', 1, 0.0)
        balance = account.get_balance()
        self.assertEqual(True, balance == 0)
        account.deposit(2000)
        balance = account.get_balance()
        assert balance == 2000
        account.withdraw(1000)
        balance = account.get_balance()
        assert balance == 1000

    def test_no_negative_withdrawal(self):
        account = Account('ken uzo', 1, 0.0)
        balance = account.get_balance()
        self.assertEqual(True, balance == 0)
        account.deposit(2000)
        balance = account.get_balance()
        assert balance == 2000
        account.withdraw(-1000)
        balance = account.get_balance()
        assert balance == 2000


    def test_cannot_withdraw_from_empty_account(self):
        account = Account('ken uzo', 1, 0.0)
        balance = account.get_balance()
        self.assertEqual(True, balance == 0)
        account.withdraw(2000)
        balance = account.get_balance()
        assert balance == 0.0


    def test_cannot_withdraw_more_than_account_balance(self):
        account = Account('ken uzo', 1, 0.0)
        balance = account.get_balance()
        self.assertEqual(True, balance == 0)
        account.deposit(1500.50)
        account.withdraw(2000)
        balance = account.get_balance()
        assert balance == 1500.50


if __name__ == '__main__':
    unittest.main()
