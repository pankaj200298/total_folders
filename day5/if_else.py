print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("printing EXAMPLE1 ")
a = 5
b = 2
c = 3
d = 4
if a < b :
    print(" 'a' is less than 'b'")
elif b<a<c<d:
     print("'b' is less than a,c, d")
else: print("unkown")

print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("printinng second example ")

num1 = int(input("please enter first number  :"))
num2 = int(input("please enter second number :"))
if num2 < num1 :
    print(f"{num1} is greater than  {num2} ")
elif num1 < num2 :
    print(f"{num2} is grater than {num1}")
elif num1 == num2  :
    print(f"{num1} and {num2} are same ")
else: print("you have intered something unexpected  ")

print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("printing example 3 ++++++++++++++ ")

roomp = ["aniket", "botre", "bala"]
friend = ["pankaj" , "falke" , "vaibhav"]
boy = 'pankaj'
if boy in roomp :
    print("this person is my room partner ")
elif boy in friend :
    print("this person is my friend ")
else: print("this boys are unknown for me ")

print("++++++++++ THE + END +++++++++++ ")