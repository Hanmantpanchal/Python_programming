#4. Write a program to enter P, T, R and calculate simple Interest.

p = int(input("enter the principle value :"))
r = int(input("enter the rate :"))
t = int(input("enter the time :"))


SI = p*r*t/100


print(f"simple intrest of given principle:{p} , time : {t} , rate :{r}  is {SI}.")