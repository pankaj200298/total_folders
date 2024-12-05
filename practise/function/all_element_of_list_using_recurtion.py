
def print_lst(list , idx=0):
    if idx == len(list):
        return
    else:
        print(list[idx])
        print_lst(list , idx +1)


lst = ['nawegaon', 'chandrapur', 'pune', 'nagpur']

print_lst(lst)