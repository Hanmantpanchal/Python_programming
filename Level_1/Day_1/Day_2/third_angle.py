#6. Write a Program to input two angles from user and find third angle of the triangle.

A1 = int(input("enter the angle 1 of a triangle :"))
A2 = int(input("enter the angle 2 of a triangle :"))


A3 = 180 - (A1+A2)

print(f"Third angle of a triagnle is {A3} .")


