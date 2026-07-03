#1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 = int(input("enter the sub1 Marks :"))
sub2 = int(input("enter the sub2 marks :"))
sub3 = int(input("enter the sub3 marks : "))
sub4 = int(input("enter the sub4 marks : "))
sub5 = int(input("enter the sub5 marks : "))


Total = sub1 + sub2 + sub3 + sub4 + sub5

Percentage = (Total/500)*100

print(f"percentage of 5 subject of student is : {Percentage}% . ")