
class student:
    def __init__(self, math , phy , chem ):
        self.math = math
        self.phy = phy
        self.chem = chem

    @property
    def percentage(self):
        return  str((self.math + self.phy + self.chem)/3 ) + " %"

stu1 = student(98,96,97)
print(stu1.percentage)

print("after updating the marks ")
stu1.phy = 86
print(stu1.percentage)