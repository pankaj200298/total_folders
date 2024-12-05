# create a account class with 2 attribute balance and account no. create a method for
# debit , credit ,  printing the balance

# attribute
account_no = 8408941618
balance = 20021998

class account:
    def __init__(self , name , saving_balance ):
        self.name = name
        self.saving_balance =  saving_balance
        print(f"your name is : {name}")
        print(f"your balance is no is : {saving_balance}")

    def credit (self, amount):
        self.saving_balance = self.saving_balance + amount
        print(f"after adding {amount} , your balance is : {balance}")

    def debit(self, amount):
        self.saving_balance = self.saving_balance - amount
        print(f"after debiting  {amount}, your balance is : {balance}")

    def printing_balance(self):
        print(f"{self.name} your balance is : {self.saving_balance}")

        
acc1 = account("pankaj", balance )
acc1.credit(98)
acc1.debit(98)
acc1.printing_balance()