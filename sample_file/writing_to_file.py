
# my_string = " im not happy "
#
# my_f = open('/home/pankaj/Desktop/testing/python/sample_file/happy.txt' , 'w+')
# my_f.write(my_string  + '\n')
# my_f.write(my_string  + '\n')
# my_f.write(my_string )
# my_f.write('\n')
# my_f.write(my_string )
# my_f.close()

# w will only for write into a file and
# a will append same thing whenevr we run the  program
#

# ex2

# my_lang = ['python', 'java' , 'c++' , 'script']
# with open('./my_fev_lang.txt' , 'w') as  my_f :
#     str_my_lang = '\n'.join(my_lang)
#     my_f.write(str_my_lang)

#ex 3
my_lang = ['python', 'java' , 'c++' , 'script', 'php']
with open('./my_fev_lang3.txt' , 'w') as  my_f :
    for i in my_lang :
        my_f.write('\n')
        my_f.write(i )