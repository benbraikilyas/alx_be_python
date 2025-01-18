class BankAccount:
    def __init__(self,display_balance=0):
        """Initialize a new bank account with an optional display_balance."""
        self.account_balance = float(display_balance)

    def deposit(self, amount):
        """Add the specified amount to the Current Balance."""
        amount = float(amount)
        if amount > 0:
            self.Current Balance += amount
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
        print(f"Current Balance: ${self.Current Balance:.2f}")
