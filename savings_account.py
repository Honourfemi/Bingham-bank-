from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    withdraw_limit = 70000

    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = 0.005

    def deposit_amount(self, amount):
        interest = amount * self.__interest_rate
        total_amount = amount + interest
        self._BankAccount__balance += total_amount  # Access balance attribute from parent class
        return self._BankAccount__balance

    def withdraw_amount(self, amount):
        if amount > SavingsAccount.withdraw_limit:
            raise ValueError("Withdrawal limit exceeded: Maximum withdrawal per instance is 70,000")
        
        if amount > self._BankAccount__balance:  # Access balance attribute from parent class
            raise ValueError("Insufficient balance")

        self._BankAccount__balance -= amount  # Withdraw amount
        return self._BankAccount__balance

    def get_balance(self):
        return self._BankAccount__balance

# Example usage
if __name__ == "__main__":
    savings_account = SavingsAccount(9096755288, "James", 85000)
    print(savings_account.deposit_amount(10000))  # Deposit with interest
    try:
        print(savings_account.withdraw_amount(72000))  # Attempt to withdraw more than limit
    except ValueError as e:
        print(e)  # Expected to print "Withdrawal limit exceeded: Maximum withdrawal per instance is 70,000"
    print(savings_account.withdraw_amount(70000))  # Withdraw within limit
    print(savings_account.withdraw_amount(15000))  # Withdraw remaining balance
