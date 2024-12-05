def fact (num):
    result =1
    while num >=1 :
        result = result * num
        num = num - 1
    return result

a = fact(3)
print(a)