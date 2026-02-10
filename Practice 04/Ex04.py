class BankAccount:
    def __init__(self,name,balance, secret):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    #Method
    def withdraw(self):
        print(f"{self.name} is withdraw money")

    def check_balance(self):
        if secret == self.__secret:
        prient(f"Remining Balance {self.__balance}")
                           


dara= BankAccount(balance="10000",name="Dara", secret="1234")
visal= BankAccount(balance="50000",name="visal", secret="12345")

#Create Object
dara = BankAccount(balance="10000", name="Dara", secret="1234")
visal = BankAccount(balance="50000", name="visal", secret="12345")

print(dara.balance)
print(visal.balance)

