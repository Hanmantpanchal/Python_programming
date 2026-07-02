#check a given number is prime or not
num = int(input("enter the number :"))
count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("It is a prime number")
else:
    print("It is not a prime number")



##check a given number is prime or not using function
def check_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
number = int(input("enter the number :"))
if check_prime(number):
    print("It is a prime number")
else:
    print("It is not a prime number")

