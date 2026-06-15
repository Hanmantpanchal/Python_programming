#Swap two numbers without using a third variable.

a=input('enter a number: ')
b=input('enter another number: ')
a,b=b,a
print('a is',a)
print('b is',b)



#other technique
a=int(input('enter a number: '))
b=int(input('enter another number: '))
a=a+b
b=a-b
a=a-b
print('a is',a)
print('b is',b)
