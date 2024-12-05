
class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"number one = {num1} , number 2 = {num2}")

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def main_menu(self):
       print(f" the addition is : {self.add()}")
       print(f" the subtraction  is : {self.sub()}")
       print(f" the division is : {self.div()}")
       print(f" the multiplication is : {self.mul()}")

cals1 = calculator(8 , 2 )
cals1.main_menu()