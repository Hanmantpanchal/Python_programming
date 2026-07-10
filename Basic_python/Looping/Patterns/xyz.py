#1 to print 10 
"""for i in range(1,11):
    for j in range(2,11):
        print(f'{j} * {i} = {j*i}', end=" \t ")
    print()
 """

for i in range(1,6):
    for j  in range(1,6):
        if(i==1 or j==1 or i==5 or j==5):
            print("*", end=" ")
        else:
            print("m",end=" ")
    print()
