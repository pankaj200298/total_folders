def state_has_no_tax(state):
    state_with_no_sales_tax = ["ak", "de", "mt", "nh", "or"]

    no_tax = None
    if state in state_with_no_sales_tax:
        no_tax = True
    else:
        no_tax = False
    return no_tax

#    if state in state_with_no_sales_tax:
#        return True
#    else:
#        return  False
#

usr_state = "or"
not_any_tax = state_has_no_tax(usr_state)
print(not_any_tax)
