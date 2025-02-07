class SbiBank:
    def user_input(self):
        print("Welcome to SBI Bank")
        print("press 1 to sign up")
        print("press 2 to login")
        print("press 3 to exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.sign_up()
        elif choice == "2":
            self.login()
        elif choice == "3":
            print("Exiting...")
        else:
            print("Invalid choice, please try again.")
            self.user_input()


    def show_balance():
      print (f"your balance is: ${balance}")
    
    def deposit():
     amount= int(input("Enter the amount you want to deposit: "))
     if amount <=0:
        print("enter a valid amount")
     else:
        return amount    

     def withdraw():
      amount= int(input("Enter the amount you want to withdraw: "))
     if amount <=0:
        print("infucient funds")
     else:
        return amount
balance=0
runing =True
print("Welcome to SBI Bank")
print("press 1 to show balance")
print("press 2 to deposit")
print("press 3 to withdraw")
print("press 4 to exit")
while runing:
 choice  = int(input("Enter your choice: "))
if choice == 1:
        show_balance()
elif choice == 2:
          balance += deposit()
elif choice == 3:
        balance -= withdraw()
    elif choice == 4:
        runing = False
    else:
        print("Invalid choice, please try again.")
 
    
