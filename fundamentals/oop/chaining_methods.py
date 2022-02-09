class users:

    def __init__(self, first_name, last_name, balance, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.balance = balance

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount > 0:
            if amount < self.balance:
                self.balance -= amount
            else:
                self.balance = 0
        return self

    def display_user_balance(self):
        if self.middle_name == None:
            return f"User: {self.first_name} {self.last_name}, Balance: {self.balance} USD"
        else:
            return f"User: {self.first_name} {self.middle_name} {self.last_name}, Balance: {self.balance} USD"


user1 = users("Jonathan", "Joestar", 100000, middle_name= "von")
user2 = users("Joseph", "Joestar", 200000)
user3 = users("Jotaro", "Kujo", 300000)


print(user1.display_user_balance())
print(user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance())




