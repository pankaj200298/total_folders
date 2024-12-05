from cloudinit.util import append_file

print("example 1 =====")
my_stuff = ["pen", "mouse", "laptop", "books"]

for a in my_stuff :
    print(a)

print("many stuff remain")

print("example 2 =====")

for b in  range(1,5) :
    print(b+1)
print("the range is over ")

print("example 3 ====")
# print the words that character of four or less
quate = "Python is an experiment in how much freedom programmers need ."
word_list = quate.split()
print(word_list)
fourw = []
for i in word_list :
    if len(i)  <= 4 :
       fourw.append(i)

print(fourw)