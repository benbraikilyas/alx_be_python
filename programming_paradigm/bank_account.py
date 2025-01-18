class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specific amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specific amount from the account if sufficient funds are available."""
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self):
        """Return the current account balance."""
        return self.__account_balance
