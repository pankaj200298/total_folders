# waf to convert $ to indian rs

def converts(x):
    rs = x * 83.88
    print(f"{x} USD = {rs} rupees ")
    return rs

converts(6)