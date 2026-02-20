class BankAccount():

 
    def __init__(self, balance, name, secret):
        self._balance = balance
        self.name = name
        self.__secret = secret
    def _verify_secret(self, secret):
        return self.__secret == secret
        
    def check_balance(self, secret):
        if secret == self.__secret:
            print(f'{self.name} remaining balance is ${self._balance}')
        else:
            print("\nIncorrect secret!")

    def withdraw(self,secret):
        amount = float(input("Enter the amount, you want to withdraw: $"))
        if self.__secret == secret:
            remain = self._balance - amount
            if remain < 0:
                print("Balance isn't enough to withdraw!")
            else:
                self._balance = remain
              
                print('| Withdraw succefully |')
         
                print(f'Your remaining balance is ${self._balance}')
    
    def deposit(self, secret):
        amount = float(input("Enter the amount, you want to deposit: $"))
        if self.__secret == secret:
            remain = self._balance + amount
            self._balance = remain
        
            print('| deposit succefully |')
           
            print(f'Your remaining balance is ${self._balance}')

    def payment(self, secret):
        print("| 1. Electricity | 2. Water | 3. Internet |")
        print('-' * 45)
        service_type = input("Enter the choice: ")
        amount = float(input("Enter the amount you want to pay: $"))
        if self.__secret == secret:
            if amount > self._balance:
                print("Insufficient balance for payment.")
            else:
                self._balance -= amount
                services = ["Electricity", "Water", "Internet"]
                
                idx = int(service_type) - 1
                if 0 <= idx < len(services):
                    service_name = services[idx]
                    print(f"Paid ${amount} for {service_name}. New balance: ${self._balance}")
                else:
                    print("Not Found Service. Try Again")

    def transfer(self, secret, account_list):
        to_name = input("Enter receiver name: ")
        amount =  float(input("Enter amount to transfer: $"))

        if self.__secret == secret:
            if amount > self._balance:
                print("Insufficient balance for transfer.")
            else:
                found = False
                for acc in account_list:
                    if acc.name == to_name:
                        acc._balance += amount
                        self._balance -= amount
                        print(f"Transferred ${amount} to {to_name} successfully!")
                        found = True
                        break
                if not found:
                    print("Receiver not found.")


class SavingAccount(BankAccount):
    
    #Method
    def check_balance(self, secret):
        if self._verify_secret(secret):
            print(f'Your old balance is ${self._balance}')
            self._balance += 10
            print(f'Your saving account has ${self._balance}')
        else:
            print("\nIncorrect secret!")


class StudentBankAccount(BankAccount):

    
    def withdraw(self, secret):
        
        amount = float(input("Enter the amount, you want to withdraw: $"))
        if amount > 500:
            print("Maximum withdrawal amount is $500!")
        elif self._BankAccount__secret == secret:
            remain = self._balance - amount
            if remain < 0:
                print("Balance isn't enough to withdraw!")
            else:
                self._balance = remain
            
                print('| Withdraw success |')
            
                print(f'Your remaining balance is  ${self._balance}')


class PremiumSaving(SavingAccount):


    def deposit(self, secret):
        amount = float(input("Enter the amount, you want to deposit: $"))
        interest = amount * 0.02
        if self._BankAccount__secret == secret:
            remain = self._balance + amount + interest
            self._balance = remain
         
            print('| deposit succefully |')
        
            print(f'Your priemiun saving account has ${self._balance} with interest 2% ${interest}  of amount')

class BusinessAccount(BankAccount):
    #Method
    def take_loan(self):
        amount = float(input("Enter the loan amount: $"))
        interest_rate = 0.7
        total_payment = amount + (amount * interest_rate / 100)
        print("Borrower Name:", self.name)
        print("Loan Amount:", amount)
        print(f'Interest Rate: {interest_rate}%')
        print("Total Payment:", total_payment)

        choice = input("Do you borrow money? (yes/no): ")
        if choice == 'yes':
            self._balance += amount
            print(f'\nYour Business Account has ${self._balance}')
        elif choice == 'no':
            return



dara = BankAccount(1000, "dara", "1234")
visal = BankAccount(2000, "phorn", "5678")
viva = SavingAccount(3000, "viva", "8765")
vanak = StudentBankAccount(1500, "kaka", "4321")
justit = PremiumSaving(5000, "lin", "9876")
kiko = BusinessAccount(12000, "jan", "0987")
account_list = [dara, visal, viva, vanak, justit, kiko]

while True:
    print('>'*86)
    print("\nWelcome to the Bank Account!\n")
    print('>'*86)
    print("| 1. Bank Account | 2. Saving Account | 3. Student Bank Account | 4. Premium Saving Account | 5. Business Account |")
    print('>'*86)
    login = input("Enter the choice: ")
    name = input("Enter your name: ")
    secret = input("Enter your secret: ")

    acc_login = None
    for acc in account_list:
        if name == acc.name and acc._verify_secret(secret):
            acc_login = acc
            break
    
    account_bank ={1:"Bank Account", 2:"Saving Account", 3:"Student Bank Account", 4:"Saving Account", 5:"Business Account"}


    if acc_login is not None:

        if login == '1' or login == '2' or login == '3' or login == '4' or login == '5':
            print(f"\nWelcome {account_bank[int(login)]}, {acc_login.name}!")
            while True:
                print('>'*86)
                print('| 1. Check Balance | 2. Withdraw | 3. Deposit | 4. Payment | 5. Transfer | 6. Exit |')
                print('>'*86)
                if login == '5':
                    print("| 7. Take Loan |")
                    print('>'*86)

                choice = input('Enter the chosse: ')
                if choice == '1':
                    print('>'*86)
                    acc_login.check_balance(secret)
                elif choice == '2':
                    print('>'*86)
                    acc_login.withdraw(secret)
                elif choice == '3':
                    print('>'*86)
                    acc_login.deposit(secret)
                elif choice == '4':
                    print('>'*86)
                    acc_login.payment(secret)
                elif choice == '5':
                    print('>'*86)
                    acc_login.transfer(secret, account_list)
                elif choice == '6':
                    print('>'*86)
                    print("Exiting... Thank you for using our service!")
                    break
                elif choice == '7' and login == '5':
                    print('>'*86)
                    acc_login.take_loan()
                else:
                    print('>1'*86)
                    print("Enter the correct chosse, again!!")

    else:
            print("\nIncorrect secret!")