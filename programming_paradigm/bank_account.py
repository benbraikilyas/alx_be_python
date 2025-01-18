class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """Initialize the bank account with account holder's name and initial balance."""
        self.__account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount: float):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        """Withdraw money from the account."""
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance is {self.__balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Return the current balance."""
        return self.__balance

    def get_account_holder(self):
        """Return the account holder's name."""
        return self.__account_holder

    def __str__(self):
        """Return a string representation of the account."""
        return f"Account Holder: {self.__account_holder}, Balance: {self.__balance}"





from bank_account import BankAccount

def main():
    # Create a BankAccount object with initial details
    account = BankAccount("Alice", 100.0)

    print("Welcome to the Bank Account System")
    print(account)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current balance: {account.get_balance()}")
        elif choice == "4":
            print("Thank you for using the Bank Account System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

