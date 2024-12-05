
def adding_f (a, b):
    total = a + b
    return total
def sub_f (a , b ):
    sub = a -b
    return sub
def mul_f (a, b):
    mul = a * b
    return mul
def div_f ( a , b):
    div = a / b if b != 0  else "cannot divisible "
    return div

val1  =  int(input("enter first no : "))
val2 = int(input("enter second no :"))
total_value = adding_f( val1 , val2)
print(f" the addition is : {total_value}")
print( sub_f(val1 , val2))
print(mul_f(val1 , val2))
print(div_f(val1 , val2))