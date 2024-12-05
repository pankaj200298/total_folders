quate = "You only live once, but if you do it right, once is enough"

small_w =  []
for_w = quate.split()
print(for_w)

for i in for_w :
    if len(i) <= 3 :
        small_w.append(i)
print(small_w)
