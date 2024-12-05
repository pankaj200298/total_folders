
print("++++++++welcome to tickit counter+++++++++++++")

theatre_name = "sapna"
age_limit = 18
print(f"welcome to {theatre_name} theatre")
print("this is the R-rated movie movie ")

your_age = int(input("please enter your age : "))
print(f"you have enter your age is {your_age} ")

if your_age >= age_limit :
    print("enjoy the movie")
else:
    adult_present =  input("is any adult with you please enter yes or no : ")
    if adult_present.lower() == "yes" :
        print("okey you can watch the movie ")
    else:
        print("sorry you have to grow up ")
