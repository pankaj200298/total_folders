# classes are user define blueprint or prototype
# objects of your class
# self keyword is mandatory for calling variable into method

class  calculator :
     num = 100
     # class variable
     # its a nothing but which variable u define inside class is .......
     # class variable is constance through the class however instance variable
     # may be differ

     # default  constructor is called
     def __init__(self, num1 , num2):
         # slf is nothing but object reference

         print("iam called automatically when object is created ")
         self.num1 = num1 #instance variable
         print(f"number one is the {num1}")
         self.num2 = num2
         print(f"number two is the {num2}")
         # the variable which define inside the constructor is called ....

         
     def getData(self):
         print("iam now executing as method in class :==> {default constructor }")

c1 = calculator( 100 ,2000) #syntax to  create objects in python
c1.getData()
# object dot (.) is the method to call the method or variable
#
print(c1.num)
