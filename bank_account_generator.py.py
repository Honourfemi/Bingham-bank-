import random
import string

class BankAccount:
    def __init__(self, account_number=None):
        self.account_number = account_number or self.generate_account_number()

    def generate_account_number(self):
        return ''.join(random.choices(string.digits, k=10))

    def __str__(self):
        return f'BankAccount(account_number={self.account_number})'

# Testing the BankAccount class
account1 = BankAccount()
print(account1)  # Predefined account number

