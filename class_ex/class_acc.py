# create a account class with 2 attribute balance and account no. create a method for
# debit , credit ,  printing the balance

balance =200298
acc_no = 8408941618

class account:
    def __init__(self, name , saving_balance , acc_no):
        self.name = name
        self.saving_balance = saving_balance
        self.acc_no = acc_no
        print(f"name of acc_hoder : {name}")
        print(f"your saving balnce is {saving_balance}")

    def debit (self , ammount ):
        self.saving_balance  =  self.saving_balance - ammount
        print(f"addter debit {ammount} your curent balnce is {self.saving_balance}")

    def credit(self, amount):
        self.saving_balance = self.saving_balance + amount
        print(f"after cerdit {amount} your current balance is {self.saving_balance}")

    def printing_balance(self):
        print(f"printing your balance ...........")
        print(f"your balance is {self.saving_balance}")

acc1 = account("pankaj" , balance, acc_no)
acc1.credit(1000)
acc1.debit(2000)
acc1.printing_balance()

