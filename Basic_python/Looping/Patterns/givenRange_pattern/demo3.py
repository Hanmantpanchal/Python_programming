#WAP to print perfect number between given range 

Start = int(input("Enter the starting number: "))
End = int(input("Enter the ending number: "))


for i in range(Start , End+1):
    sum = 0 
    for j in range(1 , i):
        if i % j == 0:
            sum = sum + j
    if sum == i :
        print(i)