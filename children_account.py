from bank_account import BankAccount

class ChildrensAccount(BankAccount):
    def __init__(self, name, account_number, balance=0.0, interest_rate=0.007):
        super().__init__(name, account_number, balance)
        self._interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            super().deposit(amount)
            interest = amount * self._interest_rate
            self._balance += interest
            print(f"Interest earned: {interest}. New balance: {self._balance}")

    def withdraw(self, amount):
        print("Withdrawals are not allowed from a Children's account.")

# Creating instances of ChildrensAccount with specific account numbers
account1 = ChildrensAccount("samuel", 12345, 2000)

account1.deposit(50)
print(f"Balance after deposit for account {account1._account_number}: {account1._balance}")
account1.withdraw(10)

