import string
import random

list_of_domain = ['gmail.com' , 'yahoo.com', 'outlook.com', 'msn.com', 'pc.co.in']

length_of_email = 4
letter = string.ascii_lowercase
output_path = 'generated_email_list.txt'

all_email = []
for domain in list_of_domain :
    for l in range (20) :
        random_string = ''.join(random.choice(letter)for i in range (length_of_email))
        #print(random_string)
        #email = random_string + '@' + domain
        email = f"{random_string}@{domain}"
        all_email.append(email)
#
# print(all_email)
#
# print(len(all_email))
with open(output_path , 'w') as f :
    #option 1
    # for email in all_email :
    #     f.write(email)
    #     f.write(',')
    #     f.write('\n')
    #
    #
    # #option 2
    # all_email_str = ',\n'.join(all_email)
    # f.write(all_email_str)


    #option 3 best and small
    f.write(',\n'.join(all_email))