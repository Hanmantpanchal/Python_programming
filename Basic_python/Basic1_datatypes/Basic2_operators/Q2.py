#calculate simple interest

p = int(input("Enter the principal amount: "))
t = int(input("Enter the time period: "))
r = int(input("Enter the rate of interest: "))

si = (p * t * r) / 100 #formula for simple interest

print("The simple interest is: ", si)