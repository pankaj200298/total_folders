import pdb


def get_user_name (name):
    user_name = {"pankaj" : "p-c",
                 "aniket" : "a-n",
                 "bala" : "b-l"
                 }
    print(f"the user {user_name[name]} is logged in ")

    return user_name[name]

user1 = get_user_name("pankaj")
print(f'user 1 is : {user1}')
pdb.set_trace()

user2 = get_user_name("aniket")
print(f"user 2 is : {user2}")
pdb.set_trace()

print("=== === === === === THE END === === === === === ")