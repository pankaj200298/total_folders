

sample_files = '/home/pankaj/Desktop/testing/python/sample_file/sate_list.txt'

with open (sample_files, 'r') as f:

 contris = f.read ()
 contry = contris.split("\n")
#  list_of_c = [i.strip() for i in contris]
# print(list_of_c)
print("=== === === === === === === === === === === === === === ===")
print(contris)
print("=== === === === === === === === === === === === === === ===")
print(contry)