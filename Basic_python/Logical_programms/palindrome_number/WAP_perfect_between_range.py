#WAP to print perfect numbers between given range 

start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))

for i in range(start,end+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(i)
        