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

class User:

    def __init__(self, first_name, last_name, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.savings = BankAccount(0.07, 500000)
        self.checking = BankAccount(0.14, 1000000)

    def savings_deposit(self, amount):
        if amount > 0:
            self.savings.balance += amount
        return self

    def savings_withdraw(self, amount):
        if amount > 0:
            if amount < self.savings.balance:
                self.savings.balance -= amount
            else:
                self.savings.balance = 0
        return self
    
    def checking_deposit(self, amount):
        if amount > 0:
            self.checking.balance += amount
        return self

    def checking_withdraw(self, amount):
        if amount > 0:
            if amount < self.checking.balance:
                self.checking.balance -= amount
            else:
                self.checking.balance = 0
        return self

    def display_checking_info(self):
        if self.middle_name == None:
            return f'User: {self.first_name} {self.last_name}, Checking Balance: {"%.2f"%self.checking.balance}'
        else:
            return f'User: {self.first_name} {self.middle_name} {self.last_name}, Checking Balance: {"%.2f"%self.checking.balance}'
    
    def display_savings_info(self):
        if self.middle_name == None:
            return f'User: {self.first_name} {self.last_name}, Savings Balance: {"%.2f"%self.savings.balance}'
        else:
            return f'User: {self.first_name} {self.middle_name} {self.last_name}, Savings Balance: {"%.2f"%self.savings.balance}'


#bonus included
user1 = User("Alex", "Schmidt")
print(user1.display_savings_info())
print(user1.savings_deposit(500000).display_savings_info())
print(user1.display_checking_info())
print(user1.checking_withdraw(500000).display_checking_info())

