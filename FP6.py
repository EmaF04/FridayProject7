class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number  # Account number
        self.balance = 0.0  # Initial balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """Check the current balance."""
        print(f"Current balance: ${self.balance:.2f}")


def main():
    # Create a bank account instance
    account_number = input("Enter your account number: ")
    account = BankAccount(account_number)

    while True:
        print("\nOptions:")
        print("a) Deposit Money")
        print("b) Withdraw Money")
        print("c) Check Balance")
        print("d) Exit")

        choice = input("Choose an option (a/b/c/d): ").strip().lower()

        if choice == 'a':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 'b':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 'c':
            account.check_balance()
        elif choice == 'd':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main function
main()
