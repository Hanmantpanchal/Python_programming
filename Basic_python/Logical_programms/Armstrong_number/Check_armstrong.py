#WAP to print the given number is Armstrong or not

num = int(input("enter the number :"))

count=0
temp = num
while temp>0:
    count+=1
    temp = temp//10

temp = num
sum = 0 
for i in range(1 , count+1):
    digit = temp%10
    temp = temp//10
    sum = sum + digit**count
if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")

    




