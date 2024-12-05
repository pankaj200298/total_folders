num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

add = num1 +  num2
sub = num2 - num1
mul = num2 * num1
div = num1 / num2 if num2 != 0 else "cannot divided by zero "

print(f"the add of two no is {add} ")
print(f"the sub of two no is {sub}")
print(f"the div of two no is {div}")