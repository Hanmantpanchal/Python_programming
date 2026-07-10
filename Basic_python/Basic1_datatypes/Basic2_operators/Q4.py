#Calculate percentage of marks. for five subjects


sub1=int(input("Enter marks of subject 1: "))
sub2=int(input("Enter marks of subject 2: "))
sub3=int(input("Enter marks of subject 3: "))
sub4=int(input("Enter marks of subject 4: "))
sub5=int(input("Enter marks of subject 5: "))

marks = sub1+sub2+sub3+sub4+sub5
total_marks = 500
percentage = (marks/total_marks)*total_marks
print("Your percentage is: ",percentage)
