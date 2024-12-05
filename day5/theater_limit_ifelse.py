theatre_name = "sapna"
age_limit = 18

print(f"welcome to {theatre_name} and enjoy the movie ")
print("please wait for some time +++++++")

user_input = int(input("enter your age : "))
print(f"you have enter the age is  { user_input} ")

print(type(user_input))
print(type(age_limit))

if user_input >= age_limit :
    print("you allow to wach the movie ")
else:
    print("sorry you have to grow up")