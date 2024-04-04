class BankAccount:
    def _init_(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
    #withdraw account money   
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def check_balance(self):
        print(f"Your balance is ${self.balance}")



def main():
    account = BankAccount()

    while True:
        print("\nBank Account Management System")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
            print("Amount deposited successfully.")

        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)

        elif choice == '3':
            account.check_balance()

        elif choice == '4':
            account.view_transaction_history()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if _name_ == "_main_":
    main()
