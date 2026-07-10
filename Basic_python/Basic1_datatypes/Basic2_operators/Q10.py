#Find the smallest of two numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a < b:
    print(a, "is the smallest number.")
elif b < a:
    print(b, "is the smallest number.")
else:
    print("Both numbers are equal.")

