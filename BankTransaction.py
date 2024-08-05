class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful! New balance: {self.balance}"
        else:
            return "Invalid deposit amount!"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful! New balance: {self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds!"

    def send_money(self, recipient_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            return f"Transfer successful! New balance: {self.balance}"
        else:
            return "Invalid transfer amount or insufficient funds!"

def main():
    account1 = BankAccount("123456", 1000)
    account2 = BankAccount("654321", 500)

    print(account1.deposit(200))
    print(account1.withdraw(150))
    print(account1.send_money(account2, 300))

    print(f"Account 1 balance: {account1.balance}")
    print(f"Account 2 balance: {account2.balance}")
