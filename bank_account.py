class BankAccount:
    def __init__(self, name, account_number, balance=0.0):
        self._name = name.title()
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"{self._name} deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{self._name} Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number


user_1 = BankAccount("Alice", 123456789012, 25000.50)
user_2 = BankAccount("Bob", 987654321098, 25000.50)

user_1.deposit(500)
user_1.withdraw(3000000)
