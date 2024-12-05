
# variable length argument  is nothing but array
#
# def f1(*num):
#     for i in num :
#         print(i)
#         print(num)
#
# a = f1(1,5,6,6,7,8)
# # print(a)

#calculate the sum of number
#
# def f2(*num1):
#     total = 0
#     for i in num1 :
#         total = total +i
#     print(total)
#     return total
# f2(1,2,3,4,5)
#
# # we can mix the positional length argument with the variable length argument
#
# def f3(n1,*num2):
#     print(n1)
#     print(num2)
# a = f3(20, 1,2,3,4,5)

# key word argument

 #internaly it takes as dictionary ==> {k:v}

def f3(** d):
    print(d)

a =  f3( a = 20, b = 11 , c = 30 )