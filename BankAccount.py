class BankAccount:
    def __init__(self, balance=0):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance-=amount
        else:
            print("not sufficient balance to withdraw")

    def disp_bal(self):
        print("Balance amount",self.balance)







