import json
import random
from pathlib import Path

class Bank: 

    databasePath = "database.json"
    data = []

    try:
        if Path(databasePath).exists():
            with open(databasePath) as fs:
                data = json.loads(fs.read())
        else: 
            print("No database found!! creating new database....")
            with open(databasePath, "w") as fs:
                fs.write("[]")
            
    except Exception as err: 
        print(f"Error : {err}")

    @classmethod
    def __update(cls):
        with open(cls.databasePath, "w") as fs:
            fs.write(json.dumps(cls.data , indent=2))

    @classmethod
    def __accountNumberGeneration(cls):
        while True: 
            account_number = random.randint(1000000000, 9999999999)
            if all(user['accountNumber'] != account_number for user in cls.data):
                return account_number
        
#  Account creation
    def createAccount(self): 
        info = {
            "name": input("Enter your name: "), 
            "age": int(input("Enter your age: ")),
            "address" : input("Enter your full address: "), 
            "phoneNumber" : input("Enter your phone number: "), 
            "emailAddress": input("Enter your Email address: "),
            "accountNumber" : Bank.__accountNumberGeneration(), 
            "pin": input("Create 4 digit pin: "),
            "balance" : 0,
            "transaction": []
        }
        if info['age'] < 18: 
            print("\nError : Your age is below 18")
        elif len(str(info['phoneNumber'])) != 10 or not info['phoneNumber'].isdigit():
            print("\nError: Phone number must be exactly 10 digits.")
        elif len(str(info['pin'])) != 4 or not info['pin'].isdigit():
            print("\nError: PIN must be exactly 4 digits.")
        else: 
            print("\nYour account created Successfully.")
            print("\nYour information : ")
            for i in info:
                print(f"    {i} : {info[i]}")
            print("\nNote: Please note down your account number.")
            Bank.data.append(info)
            Bank.__update()

# login check
    def loginCheck(self):
        accountNumber = input("Enter your 10 digit account number: ")
        pin = input("Enter 4 digit PIN: ")
        
        for user in Bank.data:
            if str(user['accountNumber']) == accountNumber and user['pin'] == pin:
                print(f"\nHi, {user['name']}")
                return user
        print("\nError: Invalid details.")
        return None

# Account Details
    def accountDetails(self, user): 
        print("\nUser details: ")
        for key, value in user.items():
            if key not in ['pin', 'transaction']:
                print(f"  {key.capitalize()} : {value}")

# deposit
    def deposit(self, user):
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount!!")
            return
        user['balance'] += amount
        user['transaction'].append(f"Deposited ₹{amount}")
        Bank.__update()
        print(f"Successfully deposited ₹{amount}. New balance: ₹{user['balance']}")

# Withdraw
    def withdraw(self, user):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Error: Invalid amount")
        elif amount > user['balance']:
            print("Error: Insufficient balance.")
        else:
            user['balance'] -= amount
            user['transaction'].append(f"Withdrawn ₹{amount}")
            Bank.__update()
            print(f"Successfully withdrawn ₹{amount}. New balance: ₹{user['balance']}")

# Check balance
    def checkBalance(self, user):
        print(f"\nYour current balance is: ₹{user['balance']}")

# Transaction History
    def transactionHistory(self, user):
        print("\n-----------Transaction History --------------")
        if not user['transaction']:
            print("No transactions yet.")
        else: 
            for transaction in user['transaction']:
                print(f"-- {transaction}")

# Profile update
    def updateProfile(self, user):
        while True:  
            print("\nWhat you want to update: ")
            print("     1. Address")
            print("     2. Email address")
            print("     3. Phone number")
            choice = input("Enter choice: ")  
            if not choice.isdigit():
                print("Error: Enter a number.")
                continue
            choice = int(choice)
            
            if choice == 1:
                user['address'] = input("Enter new address: ")
                Bank.__update()
                break
            elif choice == 2:
                user['emailAddress'] = input("Enter new Email address: ")
                Bank.__update()
                break
            elif choice == 3:
                while True: 
                    phoneNumber = input("Enter new 10 digit mobile number: ")
                    if len(phoneNumber) != 10 or not phoneNumber.isdigit():
                        print("Error: Phone number must be exactly 10 digits.")
                    else:
                        user['phoneNumber'] = phoneNumber
                        Bank.__update()
                        break
                break
            else:
                print("Error: Invalid choice.")

# Change PIN
    def changePassword(self, user):
        oldPin = input("Enter 4 digit old PIN: ")
        if user['pin'] != oldPin:
            print("\nError: Invalid PIN")
            return
        newPin = input("Enter new 4 digit PIN: ")
        if len(newPin) != 4 or not newPin.isdigit():
            print("\nError: PIN must be exactly 4 digits.")
            return
        user['pin'] = newPin
        Bank.__update()
        print("\nPIN updated Successfully.")

# logout
    def logout(self):
        print("\nYou have been logged out securely. Have a great day!")

# Main
user = Bank()
while True: 
    print("\nMenu: ")
    print(" 1. Create account")
    print(" 2. Login")
    print(" 3. Exit")
    try:  
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Error: Enter a valid number.")
        continue

    if choice == 1:
        user.createAccount()
    elif choice == 2:
        loggedUser = user.loginCheck()
        if loggedUser:
            while True:
                print("\n--- Bank Menu ---")
                print(" 1. Account Details")
                print(" 2. Deposit")
                print(" 3. Withdraw")
                print(" 4. Update Profile")
                print(" 5. Check Balance")
                print(" 6. Transaction History")
                print(" 7. Change Password")
                print(" 8. Logout")
                try:
                    opt = int(input("Enter your choice: "))
                except ValueError:
                    print("Error: Enter a valid number.")
                    continue

                if opt == 1:
                    user.accountDetails(loggedUser)
                elif opt == 2:
                    user.deposit(loggedUser)
                elif opt == 3:
                    user.withdraw(loggedUser)
                elif opt == 4:
                    user.updateProfile(loggedUser)
                elif opt == 5:
                    user.checkBalance(loggedUser)
                elif opt == 6:
                    user.transactionHistory(loggedUser)
                elif opt == 7:
                    user.changePassword(loggedUser)
                elif opt == 8:
                    user.logout()
                    break
                else:
                    print("Error: Invalid choice.")
    elif choice == 3:
        print("\nSession ended successfully.")
        break
    else:
        print("\nError: Invalid choice.")
