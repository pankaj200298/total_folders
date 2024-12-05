

input_file  = 'new_gen_email.2.txt'
output_file = 'count_of_domain_name.txt'

def  get_email_form_path ( file_path ):
    with open( file_path , 'r') as reading_file :
       raw_emails =  reading_file.readlines()
    # this option is only for to remove ',' and '\n'
    emails_clean = [ i.strip(',\n') for i in raw_emails]
    return emails_clean


def count_of_domain (list_of_email):
    #for option 1
    email_count = dict() # we create a dictionary to store the domain as key and no as value
    for email in list_of_email :
        domain = email.split('@')[-1]
        if domain in email_count.keys():
            email_count[domain] = email_count[domain] + 1
        else:
             email_count[domain] = 1
    return email_count

email_list = get_email_form_path (input_file)
count = count_of_domain (email_list)
print(count)

with open( output_file , 'w') as f :
    f.write (str(count))





















