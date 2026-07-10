#count digit 

digit = int(input("Enter the number: "))
count = 0
while digit > 0:
    digit = digit // 10
    count += 1
print("The number of digits in the number is:", count)