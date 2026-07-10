n=7
for i in range(1 , 6):
   
    for j in range(1 , i+1):
        print(j , end=" ")

    for j in range(1 , n+1):
        print(" " , end=" ")
    n = n-2

    for k in range(i , 0 , -1):
        if k != 5:
            print(k, end=" ")


    print()