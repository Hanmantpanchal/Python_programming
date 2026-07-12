#print first n prime number 

n = int(input("Enter a number: "))

count = 0

i = 2

while count < n:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1
    i += 1


##print first n prime number using function 

def print_prime(n):
    count = 0
    i = 2
    while count < n:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            count += 1
        i += 1

num = int(input("Enter a number: "))
print_prime(num)
