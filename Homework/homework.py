class BankAccount:
    # constructor
    def __init__(self, balance, name, secret):
        self.__balance = balance
        self.name = name
        self.__secret = secret

    def _receive_money(self, amount):
        self.__balance += amount

    # --- Methods ---
    def Check_Balance(self, secret):
        if self.__secret == secret:
            print(f"{self.name} remaining balance is {self.__balance}")
        else:
            print("Incorrect secret")

    def withdraw(self, secret):
        amount = float(input("Enter the amount you want to withdraw: "))
        if self.__secret == secret:
            remain = self.__balance - amount
            if remain < 0:
                print("Balance isn't enough to withdraw")
            else:
                self.__balance = remain
                print("Withdraw succesfully.")
                print(f"Your remaining balance is {self.__balance}")
        else:
            print("Invalid secret.")

    def deposit(self, secret):
        amount = float(input("Enter the amount you want to deposit: "))
        if self.__secret == secret:
            remain = self.__balance + amount
            if remain < 0:
                print("Balance isn't enough to deposit")
            else:
                self.__balance = remain
                print("deposit succesfully.")
                print(f"Your remaining balance is {self.__balance}")
        else:
            print("Invalid secret.")

    def payment(self):
        service_type = input("Enter | 1. Electricity | 2. Water | 3. Internet | :")
        amount = float(input("Enter the amount you want to pay: "))

        if amount > self.__balance:
            print("Insufficient balance for payment.")
        else:
            self.__balance -= amount
            services = ["Electricity" "Water", "Internet"]
            services = ["Electricity", "Water", "Internet"]

            idx = int(service_type) - 1 
            service_name = services[idx]
            if idx < 2:
                idx = int(service_type) - 1
            if 0 <= idx < len(services):
                service_name = services[idx]
                print(f"Paid ${amount} for {service_name}. New balance: ${self.__balance}")
            else:
                print("Not Found Service. Try Again")


    def transfer(self, to_name, amount, secret, account_list):
        if secret != self.__secret:
            print("Incorrect secret!")
            return

        if amount > self.__balance:
            print("You don't have enough money!")
            return

        receiver = None
        for acc in account_list:
            if acc.name == to_name:
                receiver = acc
                break

        if receiver:
            self.__balance -= amount
            receiver._receive_money(amount)
            print(f"Transferred ${amount} to {to_name} successfully!")
        else:
            print("Receiver not found.")

#Create Objects
dara = BankAccount(1000, "dara", "1234")
visal = BankAccount(2000, "visal", "12345")
account_list = [dara, visal]

print("Welcome to the Bank Account Management System!")

while True:
    name = input("\nInput Name: ")
    secret = input("Input Secret: ")

    current_acc = None
    #Login
    for acc in account_list:
        if acc.name == name and acc._BankAccount__secret == secret:
            current_acc = acc
            break

    if current_acc:
        print(f"\nWelcome, {current_acc.name}!")
        while True:
            print(80*">")
            choice = input("1. Balance | 2. Withdraw | 3. Deposit | 4. Payment | 5. Transfer | 6. Logout : ")

            if choice == "1":
                print(80*"-")
                current_acc.Check_Balance(secret)
            elif choice == "2":
                print(80*">")
                current_acc.withdraw(secret)
            elif choice == "3":
                print(80*">")
                current_acc.deposit(secret)
            elif choice == "4":
                print(80*">")
                current_acc.payment() 
            elif choice == "5":
                print(80*">")
                to_name = input("Enter receiver name: ")
                if to_name == current_acc.name:
                    print("Not found. Try Again")
                else:
                    try:
                        amt = float(input("Enter amount to transfer: "))
                        current_acc.transfer(to_name, amt, secret, account_list)

                    except ValueError:
                        print("Please enter a valid number.")
            elif choice == "6":
                print(100*">")
                print("Logging out...")
                break
    else:
        print(100*">")

class StudentBankAccount(BankAccount):

    def withdraw(self, secret):
        if secret != self._BankAccount__secret:
            print("Invalid secret.")
            return

        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount > 500:
            print("Student account cannot withdraw more than $500 at once.")
            return

        if amount > self._BankAccount__balance:
            print("Insufficient balance.")
        else:
            self._BankAccount__balance -= amount
            print(f"Withdraw successfully. Remaining balance: {self._BankAccount__balance}")