for i in range(1 , 6):
    for j in range(1 , 6-i):
        print("-",end="")
    for j in range(1 , i+1):
        print(j,end="")
    num = i
    for j in range(1 , i):
        print(num+1,end="")
        num= num+ 1
    print()