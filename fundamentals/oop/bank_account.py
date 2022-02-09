class BankAccount:

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > 0:
            if amount < self.balance:
                self.balance -= amount
            else:
                self.balance = 0
        return self

    def display_account_info(self):
        return f'Balance: {"%.2f" %self.balance}'
    
    def yield_interest(self):
        self.balance = self.balance*(1+self.int_rate)
        return self


account1 = BankAccount(0.07, 500000)
account2 = BankAccount(0.14, 1000000)
accounts = [account1,account2]
print(account1.deposit(100000).deposit(100000).deposit(100000).withdraw(500000).yield_interest().display_account_info())
print(account2.deposit(100000).deposit(100000).withdraw(100000).withdraw(100000).withdraw(100000).withdraw(500000).yield_interest().display_account_info())

#Bonus
for account in accounts:
    print(f'int_rate: {account.int_rate}, Balance: {"%.2f" %account.balance}')
