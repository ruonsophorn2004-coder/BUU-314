class BankAccount:
    def __init__(self,name,balance, secret):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    #Method
    def withdraw(self,amount,secret):
        print(f"{self.name} is withdraw money")
        if secret == self.__secret:
            #withdraw
            remain = self.balance - amount
            if remain < 0:
                print("Balance is not enough to withdraw")
            else:
                self.__balance = remain
                print("Withdraw Successfully")
                print("YOur remaining balance is {self.__balance}")
        else:
            print("Invalid Secret.Please try again")
    def check_balance(self,secret):
        if secret == self.__secret:
            print(f"Remining Balance {self.__balance}")
        else:
            print("ខ្ងុំមិនស្គាល់អ្នកទេ សូមព្យាយាមម្តងទៀត")
#Create Object
dara = BankAccount(balance="10000", name="Dara", secret="1234")
visal = BankAccount(balance="50000", name="visal", secret="12345")



#dara.change_balance(srecret="1234")
#dara.check_balance(secret="12345")

amount = int(input("Input amount: "))
secret = input("Input secret: ")
dara.withdraw(amount=float(amount),secret=secret)

