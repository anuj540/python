import re  
from datetime import datetime  

class BankAccount:
    print("Welcome to SBI Bank System!")
    input("Press Enter to continue...")
    print("Please choose an option:")
    
    def __init__(self):  
        self.users = {}       
        self.balances = {}    
        self.history = {}     
        self.account_creation = {} 
        self.owner = {} 
        self.last_name = {}
        self.DOB = {}
        self.your_account = {}
        self.choose_account_type = {}
        
    
    def is_valid_password(self, password):
        if not password[0].isupper():
            return "  First letter must be capital."
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "  Password must contain at least one special character."
        if len(password) < 8:
            return " Password must be at least 8 characters long."
        return " Password is valid!"

    def signup(self):
        username = input("Enter a username: ")  
        if username in self.users:  
            print("User already exists. Please log in.")
            return
        
        
        while True:
            password = input("Enter a password: ")
            result = self.is_valid_password(password)
            if "" in result:
                 break
            else:
                print(result)

        self.users[username] = password  
        self.balances[username] = 0  
        self.history[username] = []  
        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        self.account_creation[username] = creation_time 
        
        print(f"{username} signed up successfully on {creation_time}!")
        print("Welcome to our bank!")  
        print("To create an account, please fill the following details:")

        self.owner[username] = input("Enter your first name: ")  
        self.last_name[username] = input("Enter your last name: ")
        self.DOB[username] = input("Enter your DOB (DD-MM-YYYY): ")

        
        while True:
            account_number = input("Enter account number (max 12 digits): ")
            if len(account_number) <= 12 and account_number.isdigit():
                self.your_account[username] = account_number
                break
            else:
                print(" Invalid account number! Please enter again.")

        
        while True:
            account_type = input("Choose account type (savings/current): ").lower()
            if account_type in ["savings", "current"]:
                self.choose_account_type[username] = account_type
                break
            else:
                print(" Invalid account type! Please choose either 'savings' or 'current'.")

        print(" Account created successfully!")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users and self.users[username] == password:
            print(f" Login successful! Welcome {username}.")
            self.account_menu(username)  
        else:
            print(" Incorrect username or password.")
            input("Press Enter to continue...")  

    def account_menu(self, username):
        while True:
            print("\nChoose an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")  
            print("6. Account Creation Date")
            print("7. Show Profile")
            print("8. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.deposit(username)
            elif choice == "2":
                self.withdraw(username)
            elif choice == "3":
                self.show_history(username)  
            elif choice == "4":
                self.show_account_creation(username) 
            elif choice == "5": 
                self.show_Profile(username)
            elif choice == "6":
                print("Logging out...")
                input("Press Enter to continue")  
                break  
            else:
                print(" Invalid choice, please try again.")
                input("Press Enter to continue...")  

    def deposit(self, username):
        amount = float(input("Enter the amount you want to deposit: "))
        if amount > 0:
            self.balances[username] += amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            self.history[username].append(f"{timestamp} - Deposited ₹{amount}")  
            print(f" {amount} deposited successfully on {timestamp}. New balance: {self.balances[username]}")
        else:
            print(" Deposit amount should be positive.")
        
        input("Press Enter to continue...")  

    def withdraw(self, username):
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount > 0:
            if amount <= self.balances[username]:
                self.balances[username] -= amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
                self.history[username].append(f"{timestamp} - Withdrew ₹{amount}")  
                print(f" {amount} withdrawn successfully on {timestamp}. New balance: {self.balances[username]}")
            else:
                print(" Insufficient funds.")
        else:
            print(" Withdrawal amount must be positive.")

        input("Press Enter to continue...")  

    def show_history(self, username):
        print("\n Transaction History:")
        if self.history[username]:  
            for transaction in self.history[username]:
                print(f"- {transaction}")  
        else:
            print(" No transactions yet.")

        input("Press Enter to continue...")  

    def show_account_creation(self, username):
        print(f" Your account was created on: {self.account_creation[username]}")  
        input("Press Enter to continue...")  

    def show_Profile(self, username):
        print(f" First Name: {self.owner[username]}")
        print(f" Last Name: {self.last_name[username]}")
        print(f" DOB: {self.DOB[username]}")
        print(f" Account Number: {self.your_account[username]}")
        print(f" Account Type: {self.choose_account_type[username]}")
        print(f" Balance: {self.balances[username]}")
        input("Press Enter to continue...")
    def transfer(self, username):
        amount = float(input("Enter the amount you want to transfer: "))
        if amount > 0:
            if amount <= self.balances[username]:
                self.balances[username] -= amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
                self.history[username].append(f"{timestamp} - Transfered ₹{amount}")  
                print(f" {amount} transfered successfully on {timestamp}.")
                      
                print(" Insufficient funds.")
        else:
            print(" Transfer amount must be positive.")

        input("Press Enter to continue...")

        def show_history(self, username):
            print("\n Transaction History:")
            if self.history[username]:  
                for transaction in self.history[username]:
                    print(f"- {transaction}")  
            else:
                print(" No transactions yet.")

            input("Press Enter to continue...")

            def check_balance(self, username):
                print(f" Your current balance is: {self.balances[username]}")
                input("Press Enter to continue...")


account = BankAccount()

while True:
    print("\n Welcome to the Bank System!")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        account.signup()
    elif option == "2":
        account.login()
    elif option == "3":
        print(" Exiting... Thank you for using our bank system!")
        break
    else:
        print(" Invalid option. Please choose again.")

