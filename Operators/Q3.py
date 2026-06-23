#calculate compound intrest 

p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period: "))

ci = p * (1 + r/100) ** t # compound interest formula

print("The compound interest is: ", ci)
print("The total amount after compound interest is: ", p + ci)
print('amount after compound interest is: ')