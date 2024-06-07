from bank_account import BankAccount

class StudentAccount(BankAccount):
    def __init__(self, account_number, student_id, institution_name, balance=0.0, withdrawal_limit=2000, deposit_limit=50000):
        super().__init__(account_number, balance)
        self.student_id = student_id
        self.institution_name = institution_name
        self.proof_of_enrollment = False
        self._withdrawal_limit = withdrawal_limit
        self._deposit_limit = deposit_limit

    def deposit(self, amount):
        if amount <= self._deposit_limit:
            super().deposit(amount)
        else:
            print(f"Cannot deposit more than {self._deposit_limit} in one transaction.")

    def withdraw(self, amount):
        if amount <= self._withdrawal_limit:
            super().withdraw(amount)
        else:
            print(f"Cannot withdraw more than {self._withdrawal_limit} in one transaction.")

    def verify_enrollment(self, proof_document):
        # Assuming proof_document is a boolean for simplicity
        if proof_document:
            self.proof_of_enrollment = True
        else:
            print("Invalid proof of enrollment.")

    def get_withdrawal_limit(self):
        return self._withdrawal_limit

    def set_withdrawal_limit(self, limit):
        self._withdrawal_limit = limit

    def get_deposit_limit(self):
        return self._deposit_limit

    def set_deposit_limit(self, limit):
        self._deposit_limit = limit

    def __str__(self):
        return (f"StudentAccount(Account Number: {self._account_number}, Balance: {self._balance}, "
                f"Student ID: {self.student_id}, Institution: {self.institution_name}, "
                f"Proof of Enrollment: {'Verified' if self.proof_of_enrollment else 'Not Verified'}, "
                f"Withdrawal Limit: {self._withdrawal_limit}, Deposit Limit: {self._deposit_limit})")

# Example Usage:
# Assuming the BankAccount class has a __str__ method or similar to display account details
acc = StudentAccount("123456789", "S12345", "XYZ University")
print(acc)
acc.verify_enrollment(True)  # Verify the student status
acc.deposit(3000)  # Should print a message about exceeding deposit limit
acc.deposit(1000)  # Should successfully deposit
print(acc)
acc.withdraw(2500)  # Should print a message about exceeding withdrawal limit
acc.withdraw(1500)  # Should successfully withdraw
print(acc)
