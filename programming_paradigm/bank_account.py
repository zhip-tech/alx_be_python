class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional starting balance."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Add a positive amount of money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a positive amount if the balance is sufficient."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False

        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True

        return False  # Insufficient funds

    def display_balance(self):
        """Print the current balance formatted to 2 decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
