#8. Write a program to convert days into years, weeks and days.

Days = int(input("enter the Days : "))

Year = Days// 360 

Days = Days % 360 

Weeks = Days // 7 

Days = Days % 7


print(f" {Year} : years , {Weeks} : Weeks and {Days} : Days in given days ")

