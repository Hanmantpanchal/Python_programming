for i in range(1 , 6):
    for j in range(6-i):
        print(" " , end=" ")
    n = 1
    for j in range(1 , i+1):
        print(j, end=" ")
    n = n+1
    k = 1
    for k in range(i, 1, -1):
        print(k-1 , end=" ")
    k= k+1
    print()