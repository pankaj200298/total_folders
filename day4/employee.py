#this is a dictionary which include string , integer , and list
employee = {
             "name" : "pankaj",
              "age" : 26,
             "number": 8408941618,
          "company" : "loking for ",
           "skills" : ["python" , "shell scripting" , "linux" , "verilog", "system verilog "]
           }

e_name=employee["name"]
e_age=employee["age"]
e_number=employee["number"]
e_company=employee["company"]
e_skills= employee["skills"]
print(e_name)
print(e_age)
print(e_number)
print(e_company)
print(e_skills)
print(type(e_skills))
usr_skills_count = len(e_skills)
print("{} has {} skills".format(e_name, usr_skills_count))