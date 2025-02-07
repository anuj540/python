from datetime import datetime  
class BankAccount:
    def __init__(self):  
        self.users = {}       
        self.balances = {}    
        self.history = {}     
        self.account_creation = {}  
    def signup(self):
        username = input("Enter a username: ")  
        if username in self.users:  
            print("User already exists. Please log in.")
        else:
            password = input("Enter a password: ")  
            self.users[username] = password  
            self.balances[username] = 0  
            self.history[username] = []  
            creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            self.account_creation[username] = creation_time 
            print(f"User {username} signed up successfully on {creation_time}!")
            input("Press Enter to continue...")    

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users and self.users[username] == password:
            print(f"Login successful! Welcome {username}.")
            self.account_menu(username)  
        else:
            print("Incorrect username or password.")
            input("Press Enter to continue...")  

    def account_menu(self, username):
        while True:
            print("\nChoose an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transaction History")  
            print("4. Account Creation Date")
            print("5. Logout")

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
                print("Logging out...")
                input("Press Enter to continue...")  
                break  
            else:
                print("Invalid choice, please try again.")
                input("Press Enter to continue...")  

    def deposit(self, username):
        amount = float(input("Enter the amount you want to deposit: "))
        if amount > 0:
            self.balances[username] += amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            self.history[username].append(f"{timestamp} - Deposited ₹{amount}")  
            print(f"{amount} deposited successfully on {timestamp}. New balance: {self.balances[username]}")
        else:
            print("Deposit amount should be positive.")
        
        input("Press Enter to continue...")  

    def withdraw(self, username):
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount > 0:
            if amount <= self.balances[username]:
                self.balances[username] -= amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
                self.history[username].append(f"{timestamp} - Withdrew ₹{amount}")  
                print(f"{amount} withdrawn successfully on {timestamp}. New balance: {self.balances[username]}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

        input("Press Enter to continue...")  
    def show_history(self, username):
        print("\nTransaction History (Only Deposits & Withdrawals with Date & Time):")
        if self.history[username]:  
            for transaction in self.history[username]:
                print(f"- {transaction}")  
        else:
            print("No transactions yet.")

        input("Press Enter to continue...")  

    def show_account_creation(self, username):
        print(f"Your account was created on: {self.account_creation[username]}")  
        input("Press Enter to continue...")  


# Main Menu
account = BankAccount()

while True:
    print("\nWelcome to the Bank System!")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        account.signup()
    elif option == "2":
        account.login()
    elif option == "3":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid option. Please choose again.")
       
