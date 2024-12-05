
import pdb
sample_files = '/home/pankaj/Desktop/testing/python/sample_file/sate_list.txt'

my_file = open(sample_files, "r")
content = my_file.readline()
my_file.close()

#pdb.set_trace()
content_list = content.split("\n")
print(content_list)

print(content)
