##7. Program to Find the Roots of a Quadratic Equation


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

D = b * b - 4 * a * c

x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)

print(f"Roots of quadratic equation are {x1} and {x2}")

