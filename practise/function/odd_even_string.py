def odd_even_string(a):
    if a % 2 == 0:
        print(f"{a} is a EVEN NUMBER ")
    else:
        print(f"{a} is a ODD NUMBER ")

num1 = int(input("please enter any number : "))
print(f"you have enter the num is {num1}")
odd_even_string(num1)
