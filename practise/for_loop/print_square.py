#print the square of 1 to 10

i = 1

square =[]
for i in range(1, 11):
    s = i * i
    square.append(s)
    i = i+1
print(square)