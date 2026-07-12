#WAP to print perfect number between two range

start = int(input('enter the start range: '))
end = int(input('enter the end range: '))

for num in range(start,end+1):
    sum = 0
    for i in range(1,num):
        if(num%i==0):
            sum = sum+i
    if(sum==num):
        print(num)