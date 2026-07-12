#check a given number is palindrome or not

for i in range(1 , 4):
    number = int(input("enter the number : "))
    temp = number 

    revers = 0 

    while temp>0:
        d = temp % 10 
        temp = temp // 10 
        revers = (revers * 10) + d


    if revers == number:
        print("palindrome number")
    else:
        print("not a palindrome number")
else:
    if i == 4:
        print("your limit is over to check palindrome number")




##check a given number is palindrome or not using function
def check_palindrome(number):
    temp = number 

    revers = 0 

    while temp>0:
        d = temp % 10 
        temp = temp // 10 
        revers = (revers * 10) + d


    if revers == number:
        print("palindrome number")
    else:
        print("not a palindrome number")
n = int(input("enter the number :"))
check_palindrome(n)

