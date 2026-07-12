#WAP to print first n armstrong numbers

num = int(input("enter the number :"))

count=0

temp = num
n= 1 


while(temp>0):
    count = count+1
    temp = temp//10

    temp = num
    sum = 0
    while(temp>0):
        digit = temp%10
        sum = sum + digit**count
        temp = temp//10
        if(sum==num):
            print(num)
            count = count+1
            n = n+1

