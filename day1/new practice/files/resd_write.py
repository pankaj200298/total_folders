with open('test.txt') as file :
# print(file.read())

# write a program to read the line by line by using readline

# line = file.readline()
# while line !="" :
#     print(line)
#     line = file.readline()

 for i in file.readlines():
    print(i)