def north_state (state):
    north_side = ["telangana","andhra pradesh", "karnataka", "kerala"]
    print(f"this state are on north side : {north_side}")
    state_side = None
    if state in north_side :
        state_side = True
    else:
        state_side = False
    return state_side
user_state = "kerala"

india_state = north_state(user_state)
print(f"user has enter the state is : {user_state}")
print(india_state)
