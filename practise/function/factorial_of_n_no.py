# waf to print a factorial of n number
fact= 1
def factorial(n):
    global fact
    for i in range(1 , n+1):
        fact = fact * i
        print(fact)


factorial(5)