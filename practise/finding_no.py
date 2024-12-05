
# find the index no of 36 in given tuple


num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36)
x = 36
i = 0
while i < len(num) :
    if num[i] == x:
        print(f"found at the idx {i}")
    else:
        print(f"finding at {i} the idx but not found")
    i = i+1