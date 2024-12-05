# print tje multiplication table of n number

print("please enter the number for which do you want to print the table")
num = int(input("enter the no : "))
print(f"printing the tabl of : {num}")

i = 1
while i <= 10 :
    print(f"{num} * {i}  =  {num * i }")
    i=i+1
print("the table is complete ")