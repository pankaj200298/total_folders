

# waf to print sum 0f all natural no using recurtion in python
def sum_of_n_no(n):
    if n == 0 :
        return 0
    else:
     return  n + sum_of_n_no(n - 1)

print(sum_of_n_no(10))