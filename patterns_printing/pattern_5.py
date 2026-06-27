for i in range(1,6):
    for j in range(1,6):
        if(i==1 or i==2):
            print("*" , end=" ")
        elif(i==3):
            print("$", end=" ")
        elif(i==4):
            print("#", end=" ")               
        else:
            print(j , end  = " ")
    print()