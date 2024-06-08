from bank_account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0.0, overdraft_limit=0.0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return False
        
        if self._balance - amount < -self.overdraft_limit:
            print("Insufficient funds, including overdraft limit")
            return False
        
        self._balance -= amount
        print(f"Withdrawal successful. New balance: {self._balance}")
        return True
    
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return False
        
        self._balance += amount
        print(f"Deposit successful. New balance: {self._balance}")
        return True

    def __str__(self):
        return f"CurrentAccount(account_number={self._account_number}, balance={self._balance}, overdraft_limit={self.overdraft_limit})"

# Example usage:
account = CurrentAccount("123456", balance=100.0, overdraft_limit=50.0)
account.deposit(50)
account.withdraw(120)
print(account)
