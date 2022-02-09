class users:

    def __init__(self, first_name, last_name, balance, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.balance = balance

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def make_withdrawal(self, amount):
        if amount > 0:
            if amount < self.balance:
                self.balance -= amount
            else:
                self.balance = 0
            

    def display_user_balance(self):
        if self.middle_name == None:
            return f"User: {self.first_name} {self.last_name}, Balance: {self.balance} USD"
        else:
            return f"User: {self.first_name} {self.middle_name} {self.last_name}, Balance: {self.balance} USD"

    def transfer_money(self, other_user, amount):
        temp = self.balance
        if amount < self.balance:
            self.balance -= amount
            other_user.balance += amount
        else:
            other_user.balance += temp
            self.balance = 0

user1 = users("Jonathan", "Joestar", 100000, middle_name= "von")
user2 = users("Joseph", "Joestar", 200000)
user3 = users("Jotaro", "Kujo", 300000)

# print(user1.display_user_balance())
# user1.make_deposit(100000)
# print(user1.display_user_balance())
# user1.make_deposit(100000)
# print(user1.display_user_balance())
# user1.make_deposit(100000)
# print(user1.display_user_balance())
# user1.make_withdrawal(200000)
# print(user1.display_user_balance())

# print(user2.display_user_balance())
# user2.make_deposit(200000)
# print(user2.display_user_balance())
# user2.make_deposit(200000)
# print(user2.display_user_balance())
# user2.make_withdrawal(200000)
# print(user2.display_user_balance())
# user2.make_withdrawal(200000)
# print(user2.display_user_balance())


# print(user3.display_user_balance())
# user3.make_deposit(300000)
# print(user3.display_user_balance())
# user3.make_withdrawal(300000)
# print(user3.display_user_balance())
# user3.make_withdrawal(200000)
# print(user3.display_user_balance())
# user3.make_withdrawal(200000)
# print(user3.display_user_balance())

# print(user1.display_user_balance())
# print(user3.display_user_balance())
# user1.transfer_money(user3, 200000)
# print(user1.display_user_balance())
# print(user3.display_user_balance())


# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $250
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

