class Bank_account :
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.account_number = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return f"Account Balance: {self.balance}"

account = Bank_account("poorya hamidian", "123456789", 1000)
print(account.get_balance())
account.deposit(500)
account.withdraw(200)
print(account.get_balance())


