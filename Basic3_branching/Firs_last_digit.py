#find first and last digit of a number

num = int(input("Enter the number: "))


if num < 10:
    print("First and last digit is same")
else:
    first_digit = num
    last_digit = num % 10
    while first_digit >= 10:
        first_digit = first_digit // 10
    print("First digit is: ", first_digit)
    print("Last digit is: ", last_digit)