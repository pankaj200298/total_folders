# str1 = "pune"
# print(str1[::2])
# #this is the method  to print the even indexed element
#
# str2 = " one two three four five six "
# str3 = str2.split()
# print(str3)
# for i in str3 :
#     s1 = (str3[::-1])
# print(s1)

s1 ={1,2,3,4,5,6,7,8,9}
s2= {3,5,7,8}
print(s1.symmetric_difference(s2))
s2.clear()
print(s2)
print(s1.intersection(s2))
print(s1&s2)
print(s1.union(s2))
print(s1|s2)
print(s1.difference(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))
