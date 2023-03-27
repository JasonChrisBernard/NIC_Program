#Importing new module
import nic_new

#Old nic function
def old_nic(id_num):
    "this function is to process old nic details"
    gender=0
    print("NIC type : Old")
    print("You were born on",id_num[0:2])

    gender=int(id_num[2:5])

    if(gender>0 and gender<367):
        print("You are a male")
    elif(gender>500 and gender<867):
        print("You are a female")
    else:
        print("id number error")

    if id_num[9]=="V" or id_num[9]=="v":
        print("You are a voter")        
    elif id_num[9]=="X" or id_num[9]=="x":     
        print("You are a non-voter")
    else:
        print("id number error")
    


#Main body

#inizilizing variables
id_num=""
lenght=0

#getting user inputs
id_num=str(input("Type your NIC number : "))


#selecting nic type
lenght=len(id_num)

if lenght==10:
    old_nic(id_num)
    
elif lenght==12:
    nic_new.new_nic(id_num)
    
