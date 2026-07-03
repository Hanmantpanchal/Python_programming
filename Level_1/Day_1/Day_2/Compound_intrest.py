#5. Write a program to enter P, T, R and calculate Compound Interest.


p = int(input("Enter the principal value: "))
r = int(input("Enter the rate: "))
t = int(input("Enter the time: "))

A = p * (1 + r/100) ** t
CI = A - p

print(f"Compound interest of principal {p}, time {t}, and rate {r} is {CI:.2f}.")
