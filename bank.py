class User:
    def __init__(self, name, account_balance=0, is_loan_available=False):
        self.name = name
        self.account_balance = account_balance
        self.is_loan_available = is_loan_available
        self.loan_amount = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.account_balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Bank is bankrupt. Cannot withdraw.")

    def check_balance(self):
        return self.account_balance

    def transfer(self, recipient, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            recipient.account_balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.name}")
        else:
            print("Bank is bankrupt. Cannot transfer.")

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self):
        if self.is_loan_available:
            if self.loan_amount == 0:
                self.loan_amount = 2 * self.account_balance
                self.account_balance += self.loan_amount
                self.transaction_history.append(f"Took a loan of ${self.loan_amount}")
            else:
                print(f"{self.name}, you already have an outstanding loan.")
        else:
            print("The bank does not offer loans at the moment.")

class Admin:
    def __init__(self):
        self.users = []

    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def total_bank_balance(self):
        total_balance = sum(user.account_balance for user in self.users)
        return total_balance

    def total_loan_amount(self):
        total_loan = sum(user.loan_amount for user in self.users)
        return total_loan

    def toggle_loan_feature(self, enable_loan):
        for user in self.users:
            user.is_loan_available = enable_loan

# Example usage:

admin = Admin()

user1 = admin.create_user("User1")
user2 = admin.create_user("User2")

user1.deposit(3000)
user2.deposit(3500)

user1.transfer(user2, 1000)
user2.withdraw(700)

user1.take_loan()
user1.take_loan()

admin.toggle_loan_feature(True)

user2.take_loan()

print(f"User1's Account Balance: ${user1.check_balance()}")
print(f"User2's Account Balance: ${user2.check_balance()}")
print(f"Total Bank Balance: ${admin.total_bank_balance()}")
print(f"Total Loan Amount: ${admin.total_loan_amount()}")
print("=======Transaction History for User1:=======")
for transaction in user1.check_transaction_history():
    print(transaction)
print("=======Transaction History for User2:=======")
for transaction in user2.check_transaction_history():
    print(transaction)
