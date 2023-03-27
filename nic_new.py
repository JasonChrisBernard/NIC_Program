#New nic function
def new_nic(id_num):
    "this function is to process the new nic details"
    gender=0
    print("NIC type : new")
    print("you were born on",id_num[0:4])

    gender=int(id_num[4:7])


    if(gender>0 and gender<367):
        print("You are a male")
    elif(gender>500 and gender<867):
        print("You are a female")
    else:
        print("id number error")


