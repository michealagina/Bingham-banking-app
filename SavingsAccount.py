class SavingsAccount:
    def __init__(self, account_number, customer_name, balance=0, interest_rate=0.01):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} has been deposited. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} has been withdrawn. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} has been added. New balance: ${self.balance}")

    def account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")
