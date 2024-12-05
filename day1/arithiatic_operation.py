# Write a Python program that takes two numbers from the user and
# prints the sum, difference, product, and quotient of those numbers.
#ic calculator

num1 = int(input("enter the first no : "))
num2 = int(input("enter the second no : "))

add = num1 + num2
sub = num2 - num1
multy = num2 * num1
div = num1 / num2 if num2 != 0 else "cannot divided by zero "

print(f"the addition is { add }")
print(f"the multiplication is {multy}")
print(f"the subtraction is {sub}")
print(f"the division is {div}")
