import random

  
class account():
    def __init__(self, name, user_id, currency="USD"):
        self.amount = None
        self.name = name
        self.user_id = user_id
        self.currency = currency
        self.balance = self.read_balance_from_database()
        print(f"{self.name} your current balance for user id {self.user_id} is : {self.balance}")

    def deposit(self, amount ):

        self.balance = self.balance + float(amount)
        print(f"after deposit the balance is {self.balance}")

    def withdraw(self, amount):
        self.balance = self.balance - float(amount)
        print(f"after withdraw the balance is {self.balance}")

    def generate_statement(self):
        pass

    def read_balance_from_database(self):
        return random.randrange(100, 2000)

import pdb ; pdb.set_trace()

account1 = account("pankaj" , 2002)
amount1 = float(input("enter the amount to deposit : "))
account1.deposit(amount1)
amount2 = float(input("enter the amount to withdraw : "))
account1.withdraw(amount2)
