
for i in range(1 , 6):
    
    for j in range(1 , 6-i):
        print("-",end=" ")
    n =1

    for j in range(2*i-1):
        print(chr(64+n), end=" ")
        n = n + 1
        
        
    print()