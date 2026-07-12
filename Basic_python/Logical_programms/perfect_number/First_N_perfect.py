#print first n perfect number 

num = int(input('enter a number: '))
count = 0
num = 1 
while count < num:
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        print(num)
        count = count + 1
    num = num + 1


