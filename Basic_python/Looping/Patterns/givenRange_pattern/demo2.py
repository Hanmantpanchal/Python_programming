#WAp to print palindrome number in given range 
# WAP to print palindrome numbers in a given range

Start = int(input("Enter the starting number: "))
End = int(input("Enter the ending number: "))

for i in range(Start, End + 1):

    temp = i
    rev = 0

    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10

    if i == rev:
        print(i)
    