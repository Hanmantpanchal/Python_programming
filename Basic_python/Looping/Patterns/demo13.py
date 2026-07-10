n=7
for i in range(1 , 6):
   
    for j in range(1 , i+1):
        print("*" , end=" ")

    for j in range(1 , n+1):
        print(" " , end=" ")
    n = n-2

    for k in range(1 , i+1):
        if k != 5:
            print("*" , end=" ")


    print()
n = 1
for i in range(1 , 5):
    for j in range(5-i):
        print("*" , end=" ")
    
    for j in range(n):
        print(" " , end=" ")
    n = n + 2
    for k in range(1 , 6-i):
        print("*" , end=" ")
    print()
        
