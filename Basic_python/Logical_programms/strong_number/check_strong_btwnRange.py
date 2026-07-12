#WAP to print strong number between range

start=int(input("Enter the starting number: "))

end=int(input("Enter the ending number: "))
for i in range(start,end+1):
    sum=0
    temp=i
    while temp>0:
        fact=1
        rem=temp%10
        temp=temp//10
        for j in range(1,rem+1):
            fact=fact*j
        sum=sum+fact
        
    if sum==i:
        print(i)