### Encapsulation 

Encapsulation is a principle that involves bundling the data (attributes) and methods (functions) into a single unit, which is a class. It also involves restricting access to some of the object's components, which helps to protect the internal state of the object and control how it can be accessed or modified.

For example, think of a class as a box that contains both data and the operations that can be performed on that data. You only interact with the data through well-defined methods, which ensures that the data is used correctly and safely.

### Example of Encapsulation

Here's a simple Python example demonstrating encapsulation:

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance

# Using the BankAccount class
account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Attempting to access private attributes directly (not recommended)
print(account.__balance)  # This will raise an AttributeError
