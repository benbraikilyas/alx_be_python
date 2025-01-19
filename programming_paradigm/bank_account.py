class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a new bank account with an optional initial balance."""
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        amount = float(amount)
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        Withdraw the specified amount if sufficient funds are available.
        Returns True if successful, False otherwise.
        """
        amount = float(amount)
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")







import sys
from bank_account import BankAccount

def main():
    # Initialize bank account with $100 starting balance
    account = BankAccount(100)  

    # Check for proper command line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and optional amount parameter
    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    # Execute the requested operation
    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
