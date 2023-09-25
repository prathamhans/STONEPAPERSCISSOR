import random 

comp=random.randint(0,2)
user=int(input("enter 0 for stone,enter 1 for paper and enter 2 for scissor : "))

if user > 2:
    print("invalid input")
else:
    def abc(comp,user):
        if(comp==user):
           return 0
        if (comp== 2 and user==1):
            return -1
        if(comp==0 and user ==2):
            return -1
        if(comp==1 and user ==0):
            return -1

        return 1
    count=abc(comp,user)
   
    if (user==2):
        print(f"you choose {user} this was scissor")
    elif(user==1):
        print(f"you choose  {user} this was paper")
    else:
        print(f"you choose {user} this was stone")

    if (comp==2):
        print(f"comp choose {comp} this was scissor")
    elif(comp==1):
        print(f"comp choose {comp} this was paper")
    else:
        print(f"comp choose {comp} this was stone")   
    if (count==0):
        print(" its draw")
    elif(count==1):
        print("you win")
    else:
        print("YOU lose")
    

