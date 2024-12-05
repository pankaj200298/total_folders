import  string
import  random


list_of_domain = ['gmail.com' , 'yahoo.com', 'outlook.com', 'mns.com', 'pc.co.in']

length_of_email = 4
letter = string.ascii_lowercase


all_gen_email = []

for le in range(100):
     random_string = ''.join(random.choice(letter) for i in range(length_of_email))
     domain = random.choice(list_of_domain)
     email =  f"{random_string}@{domain}"
     all_gen_email.append(email)
     print(len(all_gen_email))

with open('new_gen_email.2.txt', 'w' ) as f :
     f.write(',\n'.join (all_gen_email))