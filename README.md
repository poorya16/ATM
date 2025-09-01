Here’s a clean **README.md** for your `Bank_account` class project:

---

# Bank Account 💳

This project implements a simple **Bank Account** system in Python, allowing users to deposit, withdraw, and check their balance.

## Features 🚀

* Create a new bank account with:

  * `name` (account holder’s name)
  * `account_number`
  * `initial_amount` (starting balance)
* Deposit money (only positive amounts allowed)
* Withdraw money (only if sufficient balance exists)
* Get current account balance

## Code Example 📝

```python
class Bank_account:
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
```

## Usage ▶️

```python
# Create an account
account = Bank_account("Poorya Hamidian", "123456789", 1000)

# Check balance
print(account.get_balance())  
# Output: Account Balance: 1000

# Deposit money
account.deposit(500)  
# Output: Deposited 500. New balance: 1500

# Withdraw money
account.withdraw(200)  
# Output: Withdrew 200. New balance: 1300

# Final balance
print(account.get_balance())  
# Output: Account Balance: 1300
```

## Future Improvements 🔮

* Add account types (e.g., savings, checking)
* Implement interest rates
* Add transaction history
* Secure account with PIN/password

---

گلادیاتور، می‌خوای این README رو خیلی رسمی (مناسب برای GitHub پروژه) برات بنویسم یا ساده و دوستانه مثل همین نمونه نگه دارم؟
