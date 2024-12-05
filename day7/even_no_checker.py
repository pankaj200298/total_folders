# write a program to check the no is even or odd

num = int(input("enter your number : "))

print(f"you have enter the no is {num}")

mod = num % 2

if mod == 0 :
    print(f" {num} is even " )
else:
    print(f"{num} is odd ")