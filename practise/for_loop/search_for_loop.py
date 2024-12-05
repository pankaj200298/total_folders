
num = [1,4,9,16,25,36,49,64,81,100,49]

x = 49
idx = 0
for i in num:
    if i == x:
        print(f"{x} is found at index {idx}")
    else:
        print(f"still not found and now im on index {idx} ")
    idx = idx +1