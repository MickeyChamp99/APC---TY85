class BankAccount:
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Interest:", 10000 * 5 / 100)

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Interest:", 10000 * 2 / 100)

class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        print("Fixed Deposit Interest:", 10000 * 7 / 100)

s = SavingsAccount()
c = CurrentAccount()
f = FixedDepositAccount()

s.calculate_interest()
c.calculate_interest()
f.calculate_interest()