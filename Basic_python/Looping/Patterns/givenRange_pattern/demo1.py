#print prime number in between range 

Start = int(input("Enter the starting number :"))
End = int(input("Enter the Ending number : "))

for i in range(Start , End+1):
    count = 0 
    for j in range(1 , i+1):
        if i%j==0:
            count = count + 1
    if count == 2 :
        print(i)


    