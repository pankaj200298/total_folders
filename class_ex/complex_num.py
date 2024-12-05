# write a class to addition of two complex number


class complex :
    def __init__(self , num1 , num2 ) :
        self.num1 = num1
        self.num2 = num2

    def show_num(self):
        print(f"   {self.num1} i + {self.num2} j")

    def __add__(self, comp):
        new_num1 = self.num1 + comp.num1
        new_num2 = self.num2 + comp.num2
        return complex(new_num1, new_num2)

    def __sub__(self, comp1):
        new_num1 = self.num1 - comp1.num1
        new_num2 = self.num2 - comp1.num2
        return complex(new_num1, new_num2)

    def __mul__(self, comp1):
        new_num1 = self.num1 * comp1.num1
        new_num2 = self.num2 * comp1.num2
        return complex(new_num1, new_num2)



print ("=== addition === ")

com1 = complex(6, 8 )
com1.show_num()

com2 = complex(3 , 5)
com2.show_num()
print("+ ----------")
#
# com3 = com1.add(com2)
# com3.show_num()

com3 = com1 + com2
com3.show_num()

print("=== subtraction ===")

com1 = complex(7, 9 )
com1.show_num()

com2 = complex(3 , 5)
com2.show_num()
print("- ----------")
#
# com3 = com1.add(com2)
# com3.show_num()

com3 = com1 - com2
com3.show_num()

print("=== MULTIPLICATION ===")

com1 = complex(7, 9 )
com1.show_num()

com2 = complex(3 , 5)
com2.show_num()
print("* ----------")
#
# com3 = com1.add(com2)
# com3.show_num()

com3 = com1 * com2
com3.show_num()
