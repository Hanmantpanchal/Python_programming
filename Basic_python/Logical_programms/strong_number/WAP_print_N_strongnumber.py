#WAP to print first N strong numbers

n=int(input('enter the number of strong numbers: '))

count=0

num = 1

while count<n:
    sum=0
    temp=num
    while temp>0:
        d=temp%10
        temp=temp//10
        fact=1
        for i in range(1,d+1):
            fact=fact*i
        sum=sum+fact
        
    if sum==num:
        print(num)
        count=count+1
    num=num+1
