class Bank:
    type = "Savings"

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.type

    def __repr__(self):
        print("Welcome to the SBI ATM machine")
        account_pin = input("Please enter your pin number: ")

        if account_pin == "1234":
            print("Welcome", self.name)
            return f"Login successful! (Name: {self.name}, Account: {self.Account_Number})"
        else:
            print("Pin Incorrect. Please try again")
            return self.error()

    def error(self):
        account_pin = input("Please enter your pin number: ")

        if account_pin == "1234":
            print("Welcome", self.name)
            print("Your Card Number is XXXX XXXX XXXX 1234")
            print("Would you like to Deposit / Withdraw / Check Balance?")
            print("""
1) Balance
2) Withdraw
3) Deposit
4) Quit
""")
            self.options()
        else:
            print("Pin Incorrect. Please try again")
            return self.error()

    def options(self):
        option = input("Please enter your choice: ")

        if option == "1":
            self.balanceCheck()
        elif option == "2":
            self.withdraw()
        elif option == "3":
            self.deposit()
        elif option == "4":
            print("Thank you for using our ATM.")
            exit()
        else:
            print("Invalid option. Try again.")
            self.options()

    def balanceCheck(self):
        print("Your Balance is: ", self.balance)
        self.options()

    def withdraw(self):
        amount = int(input("Please enter desired amount: "))

        if amount <= self.balance:
            self.balance -= amount
            print("Transaction success!!")
            print("Your balance is: ", self.balance)
        else:
            print("Your transaction is canceled as there is not sufficient balance.")
        self.options()

    def deposit(self):
        amount = int(input("Please enter desired amount: "))
        self.balance += amount
        print("Your transaction is successful!")
        print("Your balance is: ", self.balance)
        self.options()
obj = Bank("Nathan", 14322124, 5000)
print(obj)
