#print first n palindrome number

n=int(input('enter the number of palindrome numbers: '))
count=0
num = 0 
while count<n:
    temp = num
    rev = 0
    while temp>0:
        dig = temp%10
        rev = rev*10 + dig
        temp = temp//10
    if num==rev:
        print(num)
        count+=1
    num+=1

   
