import random
import time

def is_status_success():
    print("checking the status of process .............")
    list_to_check = [True ,True, False, False, False, False]
    bool_to_return = random.choice(list_to_check)
    return bool_to_return

def retry_with_counter_until_status_is_success( max_retry=  10 , sleep_time = 3):
    # is_success = False
    timeout = max_retry + time.time()
    counter = 0
    while time.time() <=  timeout :
        counter = counter + 1
        print(f" retry no : {time.time()}")
        is_success = is_status_success()
        print(f"the success status is : { is_success }")
        
        if is_success :
            print("the process is success...")
            break
        else:
            time.sleep(sleep_time)

    else : 
     raise Exception(f"the process does does not success after retrying {max_retry * sleep_time}")
retry_with_counter_until_status_is_success(20, 1)